"""LearnDash Authentication."""


from singer_sdk.authenticators import SimpleAuthenticator


class LearnDashAuthenticator(SimpleAuthenticator):
    """Authenticator class for LearnDash."""

    @classmethod
    def create_for_stream(cls, stream) -> "LearnDashAuthenticator":
        return cls(
            stream=stream,
            auth_headers={
                "Private-Token": stream.config.get("auth_token")
            }
        )
