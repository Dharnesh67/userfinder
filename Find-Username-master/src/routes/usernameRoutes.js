const express = require('express');
const { SocialController, EmailController, DomainController } = require('../controllers');

const router = express.Router();

router.get('/domain', DomainController);

router.post('/email', EmailController);

router.post('/social', SocialController);

module.exports = router;