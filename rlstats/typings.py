from typing import TYPE_CHECKING, Optional as NoParseOptional

import discord
from redbot.core.commands import Context

__all__ = ("GuildContext", "NoParseOptional")


if TYPE_CHECKING:

    # definition taken from redbot.core.commands.context for back-compat
    class DMContext(Context):
        """
        At runtime, this will still be a normal context object.
        This lies about some type narrowing for type analysis in commands
        using a dm_only decorator.
        It is only correct to use when those types are already narrowed
        """

        @property
        def author(self) -> discord.User:
            ...

        @property
        def channel(self) -> discord.DMChannel:
            ...

        @property
        def guild(self) -> None:
            ...

        @property
        def me(self) -> discord.ClientUser:
            ...

    # definition taken from redbot.core.commands.context for back-compat
    class GuildContext(Context):
        """
        At runtime, this will still be a normal context object.
        This lies about some type narrowing for type analysis in commands
        using a guild_only decorator.
        It is only correct to use when those types are already narrowed
        """

        @property
        def author(self) -> discord.Member:
            ...

        @property
        def channel(self) -> discord.TextChannel:
            ...

        @property
        def guild(self) -> discord.Guild:
            ...

        @property
        def me(self) -> discord.Member:
            ...


else:
    DMContext = Context
    GuildContext = Context


if not TYPE_CHECKING:

    # definition taken from redbot.core.commands.converter for back-compat
    class NoParseOptional:
        """
        This can be used instead of `typing.Optional`
        to avoid discord.py special casing the conversion behavior.
        .. warning::
            This converter class is still provisional.
        .. seealso::
            The `ignore_optional_for_conversion` option of commands.
        """

        def __class_getitem__(cls, key):
            if isinstance(key, tuple):
                raise TypeError("Must only provide a single type to Optional")
            return key
