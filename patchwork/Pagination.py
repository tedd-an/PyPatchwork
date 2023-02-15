"""
PyPatchwork - Python Library for Patchwork REST API

Copyright (C) 2023  Tedd Ho-Jeong An <hj.tedd.an@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/
"""


class Pagination:
    def __init__(
        self,
        cls,
        connection,
        next_link,
        next_params=None,
    ):
        self.__elements = list()
        self.__cls = cls
        self.__connection = connection
        self.__next_link = next_link
        self.__next_params = next_params

    def __iter__(self):
        yield from self.__elements
        while self.__next_link is not None:
            # Get next page
            new_element = self._get_next_page()
            self.__elements += new_element
            yield from new_element

    def _get_next_link(self, headers):
        links = {}
        if "Link" in headers:
            link_list = headers["Link"].split(", ")
            for link in link_list:
                url, rel = link.split("; ")
                url = url[1:-1]
                rel = rel[5:-1]
                links[rel] = url
        return links

    def _get_next_page(self):
        print(f"link: {self.__next_link}")
        headers, data = self.__connection.request(
            "GET",
            self.__next_link,
            self.__next_params,
        )
        data = data if data else []

        self.__next_link = None
        if len(data) > 0:
            links = self._get_next_link(headers)
            if "next" in links:
                self.__next_link = links["next"]
        # Can be set to None since the initial params are already included in
        # the __next_link.
        self.__next_params = None

        content = []
        for item in data:
            content.append(self.__cls(self.__connection, item))

        return content
