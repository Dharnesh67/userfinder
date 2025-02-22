function validateUsername(req, res, next) {
    try {
        const username = req.query.username;
        // console.log(username);
        if(!username) {
            return res.status(StatusCodes.BAD_REQUEST).json({message: "Please enter a valid username"});
        }

        next();
    } catch (error) {
        return error;
    }
}

module.exports = {
    validateUsername
}