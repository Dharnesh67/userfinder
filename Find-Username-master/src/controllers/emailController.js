async function emailController(req, res) {
    try {
        const { username } = req.params;
        const response = await DomainService.findUsers(username);

        if(!response) {
            throw new AppError(`No domain name found with username ${username}.`, StatusCodes.NOT_FOUND);
        }

        SuccessResponse.data = response;

        return res.status(StatusCodes.OK).json(SuccessResponse);
    } catch (error) {
        ErrorResponse.error = error;
        return res.status(StatusCodes.INTERNAL_SERVER_ERROR).json(ErrorResponse);
    }
}

module.exports = emailController;