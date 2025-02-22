const { exec } = require('child_process');
const path = require('path');
const { Paths } = require('../common');

function webNames(output) {
  const urlRegex = /https?:\/\/(?:www\.)?([^\/\s]+)/g;
  const websiteNames = new Set();
  let match;
  while ((match = urlRegex.exec(output)) !== null) {
    const domainParts = match[1].split('.');
    const name = domainParts.length > 1 ? domainParts[domainParts.length - 2] : domainParts[0];
    websiteNames.add(name.charAt(0).toUpperCase() + name.slice(1));
  }
  return Array.from(websiteNames);
}

async function scriptRunner(scriptName, __dirname, username, lang) {
  return await new Promise((resolve, reject) => {
    const scriptPath = path.join(__dirname, scriptName);
    const command = `${lang} ${scriptPath} ${username}`.trim();
    console.log("COMMAND: ", command);
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.log(__dirname);
        reject(`Error executing ${scriptName}: ${stderr}`);
      } else {
        resolve(webNames(stdout));
      }
    });
  });
}

async function executeScripts(username) {
  try {
    const { marpleDirPath, snoopDirPath, blackbirdDirPath } = Paths;

    const scripts = [
      // scriptRunner('marple.py', marpleDirPath, username, 'python'),
      // scriptRunner('snoop.py', snoopDirPath, username, 'python'),
      scriptRunner('sherlock', "", username, ""),
      // scriptRunner('blackbird.py', blackbirdDirPath, `--username ${username}`, 'python')
    ];

    const results = await Promise.all(scripts);

    const allDomains = results.flat();

    return allDomains;
  } catch (error) {
    console.error('Error executing scripts:', error);
    return [];
  }
}

module.exports = {
  executeScripts
};