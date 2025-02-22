const ToolExecutor = require('../utils/helper/tool-executor');
async function findUsers(username) {
    try {
        const response = await ToolExecutor.executeScripts(username);
        return response;
    } catch (error) {
        throw new AppError('Cant fetch the details', error);
    }
}

module.exports = {
    findUsers
};