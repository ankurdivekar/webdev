from fasthtml.components import *
from fasthtml.svg import *

content = Body(
    Div(
        Nav(
            Div(
                Img(
                    src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/leaves.png",
                    cls="h-6 w-6 mx-auto",
                ),
                cls="h-16 flex items-center w-full",
            ),
            Ul(
                Li(
                    A(
                        I(
                            Svg(
                                Path(
                                    d="M12 6.453l9 8.375v9.172h-6v-6h-6v6h-6v-9.172l9-8.375zm12 5.695l-12-11.148-12 11.133 1.361 1.465 10.639-9.868 10.639 9.883 1.361-1.465z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current h-5 w-5",
                            ),
                            cls="mx-auto",
                        ),
                        title="Home",
                        href="#home",
                        cls="h-16 px-6 flex items-center text-white bg-teal-700 w-full",
                    )
                ),
                Li(
                    A(
                        I(
                            Svg(
                                Path(
                                    d="M18.546 3h-13.069l-5.477 8.986v9.014h24v-9.014l-5.454-8.986zm-3.796 12h-5.5l-2.25-3h-4.666l4.266-7h10.82l4.249 7h-4.669l-2.25 3zm-9.75-4l.607-1h12.787l.606 1h-14zm12.18-3l.607 1h-11.573l.607-1h10.359zm-1.214-2l.606 1h-9.144l.607-1h7.931z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current h-5 w-5",
                            ),
                            cls="mx-auto",
                        ),
                        title="Views",
                        href="#views",
                        cls="h-16 px-6 flex items-center hover:text-white w-full",
                    )
                ),
                Li(
                    A(
                        I(
                            Svg(
                                Path(
                                    d="M19 7.001c0 3.865-3.134 7-7 7s-7-3.135-7-7c0-3.867 3.134-7.001 7-7.001s7 3.134 7 7.001zm-1.598 7.18c-1.506 1.137-3.374 1.82-5.402 1.82-2.03 0-3.899-.685-5.407-1.822-4.072 1.793-6.593 7.376-6.593 9.821h24c0-2.423-2.6-8.006-6.598-9.819z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current h-5 w-5",
                            ),
                            cls="mx-auto",
                        ),
                        title="Customer Lists",
                        href="#customer-lists",
                        cls="h-16 px-6 flex items-center hover:text-white w-full",
                    )
                ),
                Li(
                    A(
                        I(
                            Svg(
                                Path(
                                    d="M5 19h-4v-4h4v4zm6 0h-4v-8h4v8zm6 0h-4v-13h4v13zm6 0h-4v-19h4v19zm1 2h-24v2h24v-2z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current h-5 w-5",
                            ),
                            cls="mx-auto",
                        ),
                        title="Reporting",
                        href="#reporting",
                        cls="h-16 px-6 flex items-center hover:text-white w-full",
                    )
                ),
                Li(
                    A(
                        I(
                            Svg(
                                Path(
                                    d="M24 13.616v-3.232c-1.651-.587-2.694-.752-3.219-2.019v-.001c-.527-1.271.1-2.134.847-3.707l-2.285-2.285c-1.561.742-2.433 1.375-3.707.847h-.001c-1.269-.526-1.435-1.576-2.019-3.219h-3.232c-.582 1.635-.749 2.692-2.019 3.219h-.001c-1.271.528-2.132-.098-3.707-.847l-2.285 2.285c.745 1.568 1.375 2.434.847 3.707-.527 1.271-1.584 1.438-3.219 2.02v3.232c1.632.58 2.692.749 3.219 2.019.53 1.282-.114 2.166-.847 3.707l2.285 2.286c1.562-.743 2.434-1.375 3.707-.847h.001c1.27.526 1.436 1.579 2.019 3.219h3.232c.582-1.636.75-2.69 2.027-3.222h.001c1.262-.524 2.12.101 3.698.851l2.285-2.286c-.744-1.563-1.375-2.433-.848-3.706.527-1.271 1.588-1.44 3.221-2.021zm-12 2.384c-2.209 0-4-1.791-4-4s1.791-4 4-4 4 1.791 4 4-1.791 4-4 4z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current h-5 w-5",
                            ),
                            cls="mx-auto",
                        ),
                        title="Admin",
                        href="#admin",
                        cls="h-16 px-6 flex items-center hover:text-white w-full",
                    )
                ),
            ),
            Div(
                Img(
                    style="filter: invert(85%)",
                    src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/chi.png",
                    cls="h-8 w-10 mx-auto",
                ),
                cls="mt-auto h-16 flex items-center w-full",
            ),
            aria_label="side bar",
            aria_orientation="vertical",
            cls="flex-none flex flex-col items-center text-center bg-teal-900 text-gray-400 border-r",
        ),
        Div(
            Nav(
                Ul(
                    Li(
                        Button(
                            I(
                                Svg(
                                    Path(
                                        d="M24 10h-10v-10h-2v10h-10v2h10v10h2v-10h10z"
                                    ),
                                    xmlns="http://www.w3.org/2000/svg",
                                    width="24",
                                    height="24",
                                    viewbox="0 0 24 24",
                                    cls="fill-current w-3 h-3 mx-auto",
                                )
                            ),
                            Span("Add", cls="ml-2"),
                            aria_controls="add",
                            aria_expanded="false",
                            aria_haspopup="listbox",
                            cls="flex items-center h-full px-4 text-sm",
                        ),
                        Span(
                            Ul(
                                Li(
                                    Label("New", cls="block px-4 py-3 font-semibold"),
                                    Hr(),
                                    role="separator",
                                    cls="mb-2",
                                ),
                                Li(
                                    "Ticket",
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    "User",
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    "Organization",
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    "Search",
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    Label(
                                        "Recently Viewed",
                                        cls="block px-4 py-3 font-semibold",
                                    ),
                                    Hr(),
                                    role="separator",
                                    cls="mb-2",
                                ),
                                Li(
                                    Div(
                                        Div(
                                            Span(
                                                "O",
                                                style="padding: 2px 5px; font-size: 0.7rem",
                                                cls="font-mono rounded-sm bg-red-600 text-white leading-none",
                                            ),
                                            cls="pr-2",
                                        ),
                                        Div(
                                            P("Vertias - ams opps issue"),
                                            P(
                                                Span("#ticket/14352"),
                                                Span("�", cls="mx-1 font-black"),
                                                Span("Nico Braun"),
                                                cls="text-gray-600",
                                            ),
                                            cls="flex-1",
                                        ),
                                        cls="flex",
                                    ),
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    Div(
                                        Div(
                                            Span(
                                                "N",
                                                style="padding: 2px 5px; font-size: 0.7rem",
                                                cls="font-mono rounded-sm bg-yellow-400 text-black leading-none",
                                            ),
                                            cls="pr-2",
                                        ),
                                        Div(
                                            P("Vertias - ams opps issue"),
                                            P(
                                                Span("#ticket/14352"),
                                                Span("�", cls="mx-1 font-black"),
                                                Span("Nico Braun"),
                                                cls="text-gray-600",
                                            ),
                                            cls="flex-1",
                                        ),
                                        cls="flex",
                                    ),
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    Div(
                                        Div(
                                            Span(
                                                "S",
                                                style="padding: 2px 5px; font-size: 0.7rem",
                                                cls="font-mono rounded-sm bg-gray-500 text-white leading-none",
                                            ),
                                            cls="pr-2",
                                        ),
                                        Div(
                                            P("Vertias - ams opps issue"),
                                            P(
                                                Span("#ticket/14352"),
                                                Span("�", cls="mx-1 font-black"),
                                                Span("Nico Braun"),
                                                cls="text-gray-600",
                                            ),
                                            cls="flex-1",
                                        ),
                                        cls="flex",
                                    ),
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    Div(
                                        Div(
                                            Span(
                                                "P",
                                                style="padding: 2px 5px; font-size: 0.7rem",
                                                cls="font-mono rounded-sm bg-blue-600 text-white leading-none",
                                            ),
                                            cls="pr-2",
                                        ),
                                        Div(
                                            P("Vertias - ams opps issue"),
                                            P(
                                                Span("#ticket/14352"),
                                                Span("�", cls="mx-1 font-black"),
                                                Span("Nico Braun"),
                                                cls="text-gray-600",
                                            ),
                                            cls="flex-1",
                                        ),
                                        cls="flex",
                                    ),
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                Li(
                                    Div(
                                        Div(
                                            Span(
                                                "H",
                                                style="padding: 2px 5px; font-size: 0.7rem",
                                                cls="font-mono rounded-sm bg-gray-800 text-white leading-none",
                                            ),
                                            cls="pr-2",
                                        ),
                                        Div(
                                            P("Vertias - ams opps issue"),
                                            P(
                                                Span("#ticket/14352"),
                                                Span("�", cls="mx-1 font-black"),
                                                Span("Nico Braun"),
                                                cls="text-gray-600",
                                            ),
                                            cls="flex-1",
                                        ),
                                        cls="flex",
                                    ),
                                    role="option",
                                    cls="px-6 py-1 my-1 focus:outline-none focus:bg-blue-100 hover:bg-blue-100 cursor-pointer",
                                ),
                                id="add",
                                role="listbox",
                                cls="outline-none py-2 bg-white border rounded-md w-screen max-w-md w-dropdown-large shadow-lg focus:outline-none leading-relaxed",
                            ),
                            cls="absolute p-1 hidden group-hover:block",
                        ),
                        cls="group relative",
                    ),
                    aria_label="top bar left",
                    aria_orientation="horizontal",
                    cls="flex",
                ),
                Ul(
                    Li(
                        Input(
                            title="Search Bar",
                            aria_label="search bar",
                            role="search",
                            type="text",
                            placeholder="Search Chi Desk Support",
                            cls="pr-8 pl-4 py-2 rounded-md cursor-pointer transition-all duration-300 ease-in-out focus:border-black focus:cursor-text w-4 focus:w-64 placeholder-transparent focus:placeholder-gray-500",
                        ),
                        I(
                            Svg(
                                Path(
                                    d="M21.172 24l-7.387-7.387c-1.388.874-3.024 1.387-4.785 1.387-4.971 0-9-4.029-9-9s4.029-9 9-9 9 4.029 9 9c0 1.761-.514 3.398-1.387 4.785l7.387 7.387-2.828 2.828zm-12.172-8c3.859 0 7-3.14 7-7s-3.141-7-7-7-7 3.14-7 7 3.141 7 7 7z"
                                ),
                                xmlns="http://www.w3.org/2000/svg",
                                width="24",
                                height="24",
                                viewbox="0 0 24 24",
                                cls="fill-current w-4 h-4 mx-auto",
                            ),
                            cls="pointer-events-none absolute top-0 right-0 h-full flex items-center pr-3",
                        ),
                        cls="relative",
                    ),
                    Li(
                        Button(
                            I(
                                Svg(
                                    Path(
                                        d="M15.137 3.945c-.644-.374-1.042-1.07-1.041-1.82v-.003c.001-1.172-.938-2.122-2.096-2.122s-2.097.95-2.097 2.122v.003c.001.751-.396 1.446-1.041 1.82-4.667 2.712-1.985 11.715-6.862 13.306v1.749h20v-1.749c-4.877-1.591-2.195-10.594-6.863-13.306zm-3.137-2.945c.552 0 1 .449 1 1 0 .552-.448 1-1 1s-1-.448-1-1c0-.551.448-1 1-1zm3 20c0 1.598-1.392 3-2.971 3s-3.029-1.402-3.029-3h6z"
                                    ),
                                    xmlns="http://www.w3.org/2000/svg",
                                    width="24",
                                    height="24",
                                    viewbox="0 0 24 24",
                                    cls="fill-current w-4 h-4 mx-auto",
                                )
                            ),
                            title="Notifications",
                            aria_label="notifications",
                            cls="w-full h-full text-white bg-gray-600 rounded-md focus:outline-none focus:shadow-outline",
                        ),
                        cls="h-8 w-8 ml-3",
                    ),
                    Li(
                        Button(
                            I(
                                Svg(
                                    Path(
                                        d="M22 6v16h-20v-16h20zm2-6h-24v24h24v-24zm-11 11v1.649l3.229 1.351-3.229 1.347v1.653l5-2.201v-1.599l-5-2.2zm-7 2.201v1.599l5 2.2v-1.653l-3.229-1.347 3.229-1.351v-1.649l-5 2.201z"
                                    ),
                                    xmlns="http://www.w3.org/2000/svg",
                                    width="24",
                                    height="24",
                                    viewbox="0 0 24 24",
                                    cls="fill-current w-4 h-4 mx-auto",
                                )
                            ),
                            title="v2 REPL",
                            aria_label="repl",
                            cls="w-full h-full text-white bg-gray-600 rounded-md focus:outline-none focus:shadow-outline",
                        ),
                        cls="h-8 w-8 ml-3",
                    ),
                    Li(
                        Button(
                            I(
                                Svg(
                                    Path(
                                        d="M11 11h-11v-11h11v11zm13 0h-11v-11h11v11zm-13 13h-11v-11h11v11zm13 0h-11v-11h11v11z"
                                    ),
                                    xmlns="http://www.w3.org/2000/svg",
                                    width="24",
                                    height="24",
                                    viewbox="0 0 24 24",
                                    cls="fill-current w-5 h-5 mx-auto",
                                ),
                                cls="text-gray-600",
                            ),
                            title="Products",
                            aria_label="chi desk products",
                            cls="w-full h-full rounded-md focus:outline-none focus:shadow-outline",
                        ),
                        cls="h-8 w-8 ml-3",
                    ),
                    Li(
                        Button(
                            Img(
                                src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/me.jpg",
                                cls="h-full w-full rounded-full mx-auto",
                            ),
                            title="Page Menu",
                            aria_label="page menu",
                            cls="h-full w-full rounded-full border focus:outline-none focus:shadow-outline",
                        ),
                        cls="h-10 w-10 ml-3",
                    ),
                    aria_label="top bar right",
                    aria_orientation="horizontal",
                    cls="px-8 flex items-center",
                ),
                aria_label="top bar",
                cls="flex-none flex justify-between bg-white h-16",
            ),
            Header(
                H1("Dashboard", id="page-caption", cls="font-semibold text-lg"),
                aria_label="page caption",
                cls="flex-none flex h-16 bg-gray-100 border-t px-4 items-center",
            ),
            Main(
                Section(
                    H1("Updates to your tickets", cls="font-semibold mb-3"),
                    Ul(
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                        Li(
                            Article(
                                Span(
                                    Img(
                                        src="https://raw.githubusercontent.com/bluebrown/tailwind-zendesk-clone/master/public/assets/avatar.png",
                                        cls="h-8 w-8 rounded-md",
                                    ),
                                    cls="flex-none pt-1 pr-2",
                                ),
                                Div(
                                    Header(
                                        "Tarun T",
                                        Span("commented", cls="font-semibold"),
                                        "on",
                                        H1('"RE: WPMS issue".', cls="inline"),
                                        cls="mb-1",
                                    ),
                                    P(
                                        "Hi Mazhar, Please note this issue comes when user is not\n                    closing or logout sy…",
                                        cls="text-gray-600",
                                    ),
                                    Footer(
                                        "Friday 22:16", cls="text-gray-500 mt-2 text-sm"
                                    ),
                                    cls="flex-1",
                                ),
                                tabindex="0",
                                cls="cursor-pointer border rounded-md p-3 bg-white flex text-gray-700 mb-2 hover:border-green-500 focus:outline-none focus:border-green-500",
                            )
                        ),
                    ),
                    cls="flex flex-col p-4 w-full max-w-sm flex-none bg-gray-100 min-h-0 overflow-auto",
                ),
                Section(
                    Nav(
                        Section(
                            Label(
                                "Open Tickets",
                                Span("(current)", cls="font-normal text-gray-700"),
                                id="open-tickets-tabs-label",
                                cls="font-semibold block mb-1 text-sm",
                            ),
                            Ul(
                                Li(
                                    Button(
                                        P("6", cls="font-semibold text-lg"),
                                        P("You", cls="text-sm uppercase text-gray-600"),
                                        cls="focus:outline-none focus:bg-yellow-200 p-2 rounded-l-md border border-r-0 bg-white flex flex-col items-center w-24",
                                    )
                                ),
                                Li(
                                    Button(
                                        P("23", cls="font-semibold text-lg"),
                                        P(
                                            "Groups",
                                            cls="text-sm uppercase text-gray-600",
                                        ),
                                        cls="focus:outline-none focus:bg-yellow-200 p-2 border rounded-r-md bg-white flex flex-col items-center w-24 cursor-pointer",
                                    )
                                ),
                                cls="flex",
                            ),
                            aria_labelledby="open-tickets-tabs-label",
                            cls="mr-4 focus:outline-none",
                        ),
                        Section(
                            Label(
                                "Ticket Statistics",
                                Span("(this week)", cls="font-normal text-gray-700"),
                                id="ticket-statistics-tabs-label",
                                cls="font-semibold block mb-1 text-sm",
                            ),
                            Ul(
                                Li(
                                    Button(
                                        P("16", cls="font-semibold text-lg"),
                                        P(
                                            "good",
                                            cls="uppercase text-gray-600 text-sm",
                                        ),
                                        cls="focus:outline-none focus:bg-yellow-200 p-2 rounded-l-md border border-r-0 bg-white flex flex-col items-center w-24",
                                    )
                                ),
                                Li(
                                    Button(
                                        P("2", cls="font-semibold text-lg"),
                                        P("bad", cls="uppercase text-gray-600 text-sm"),
                                        cls="focus:outline-none focus:bg-yellow-200 p-2 border border-r-0 bg-white flex flex-col items-center w-24",
                                    )
                                ),
                                Li(
                                    Button(
                                        P("32", cls="font-semibold text-lg"),
                                        P(
                                            "solved",
                                            cls="uppercase text-gray-600 text-sm",
                                        ),
                                        cls="focus:outline-none focus:bg-yellow-200 p-2 border rounded-r-md bg-white flex flex-col items-center w-24",
                                    )
                                ),
                                cls="flex",
                            ),
                            aria_labelledby="ticket-statistics-tabs-label",
                            cls="pb-2",
                        ),
                        cls="bg-gray-100 flex p-4",
                    ),
                    Header(
                        Div(
                            H2(
                                "Tickets requiring your attention (6)",
                                id="content-caption",
                                cls="font-semibold",
                            ),
                            Span(
                                Button(
                                    "What is this?",
                                    role="details",
                                    aria_controls="info-popup",
                                    cls="text-blue-700 border-b border-dotted border-blue-700 focus:outline-none text-sm",
                                ),
                                Div(
                                    Div(
                                        Header(
                                            "People are waiting for replies!",
                                            cls="font-semibold rounded-t-lg bg-gray-300 px-4 py-2",
                                        ),
                                        Div(
                                            P(
                                                "These are new or open tickets that are assigned to you,\n                        unassinged in your group(s) or not assigned to any\n                        group.",
                                                cls="mb-4",
                                            ),
                                            P(
                                                "They are ordered by priority and requester update date\n                        (oldest first).",
                                                cls="mb-1",
                                            ),
                                            cls="p-4 border-t",
                                        ),
                                        cls="border rounded-md rounded-t-lg shadow-lg bg-white w-full max-w-xs w-screen",
                                    ),
                                    role="tooltip",
                                    id="info-popup",
                                    cls="absolute pt-1 rounded-md rounded-t-lg right-0 transform translate-x-40 mx-auto hidden group-hover:block z-50",
                                ),
                                cls="ml-3 group relative",
                            ),
                            cls="flex",
                        ),
                        Div(
                            Button(
                                "Play",
                                title="See available tickets in this view",
                                aria_label="play",
                                cls="border rounded-md px-3 py-2 leading-none",
                            ),
                            cls="ml-auto",
                        ),
                        cls="bg-white border-t flex items-center py-1 px-4",
                    ),
                    Table(
                        Thead(
                            Tr(
                                Th(
                                    Input(type="checkbox", name=True, id=True),
                                    cls="font-semibold text-left py-3 pl-3 pr-1 w-24",
                                ),
                                Th(
                                    "ID",
                                    cls="font-semibold text-left py-3 px-1 w-24 truncate",
                                ),
                                Th(
                                    "Subject",
                                    cls="font-semibold text-left py-3 px-1 w-full max-w-xs xl:max-w-lg truncate",
                                ),
                                Th(
                                    "Requester",
                                    cls="font-semibold text-left py-3 px-1 flex-1 truncate",
                                ),
                                Th(
                                    "Requester updated",
                                    cls="font-semibold text-left py-3 px-1 flex-1 truncate",
                                ),
                                Th(
                                    "Group",
                                    cls="font-semibold text-left py-3 px-1 flex-1 truncate",
                                ),
                                Th(
                                    "Assignee",
                                    cls="font-semibold text-left py-3 px-1 flex-1 truncate",
                                ),
                                cls="border-b flex",
                            ),
                            cls="flex w-full flex-col px-4",
                        ),
                        Tbody(
                            Tr(
                                Th(
                                    H2(
                                        Span("Priority", cls="font-normal mr-1"),
                                        Span("Low"),
                                        cls="text-sm",
                                    ),
                                    colspan="7",
                                    cls="bg-gray-100 text-left px-3 py-2 flex-1",
                                ),
                                cls="border-b flex",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "O",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-red-600 text-white leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Quo laudantium error corporis accusamus unde, labore\n                            quidem non officiis.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi Team,",
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Yesterday 10:33",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "Quo laudantium error corporis accusamus unde, labore\n                      quidem non officiis.",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Quo laudantium error corporis accusamus unde, labore\n                            quidem non officiis.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi Team,",
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Yesterday 10:33",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Marla Darsuz", cls="py-3 px-1 flex-1 truncate"),
                                Td("Tuesday 09:56", cls="py-3 px-1 flex-1 truncate"),
                                Td("UK Support", cls="py-3 px-1 flex-1 truncate"),
                                Td("Nico Braun", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "O",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-red-600 text-white leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Lorem ipsum dolor sit amet, consectetur adipisicing\n                            elit.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Today 13:30",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse tempora\n                            aliquam voluptates quibusdam quae debitis laboriosam\n                            iure ea quos.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "Lorem ipsum dolor sit amet, consectetur adipisicing elit.",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Lorem ipsum dolor sit amet, consectetur adipisicing\n                            elit.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Today 13:30",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse tempora\n                            aliquam voluptates quibusdam quae debitis laboriosam\n                            iure ea quos.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Jim Beam", cls="py-3 px-1 flex-1 truncate"),
                                Td("Friday 10:29", cls="py-3 px-1 flex-1 truncate"),
                                Td("UK Support", cls="py-3 px-1 flex-1 truncate"),
                                Td("Nico Braun", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "N",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-yellow-400 text-black leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "New",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-yellow-400 text-black",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Excepturi at labore vel accusamus exercitationem\n                            quam, amet provident!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(cls="font-semibold"),
                                                        P(
                                                            cls="ml-auto text-gray-700 text-sm"
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(cls="mt-2"),
                                                    cls="mt-4 hidden",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "Excepturi at labore vel accusamus exercitationem quam,\n                      amet provident!",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "New",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-yellow-400 text-black",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Excepturi at labore vel accusamus exercitationem\n                            quam, amet provident!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(cls="font-semibold"),
                                                        P(
                                                            cls="ml-auto text-gray-700 text-sm"
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(cls="mt-2"),
                                                    cls="mt-4 hidden",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Paul Ferrez", cls="py-3 px-1 flex-1 truncate"),
                                Td("Today 13:45", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "O",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-red-600 text-white leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "impedit possimus praesentium voluptatum omnis\n                            assumenda rem autem magni consequatur nostrum\n                            distinctio unde.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi Team,",
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Yesterday 10:33",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "impedit possimus praesentium voluptatum omnis assumenda\n                      rem autem magni consequatur nostrum distinctio unde.",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Low)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "impedit possimus praesentium voluptatum omnis\n                            assumenda rem autem magni consequatur nostrum\n                            distinctio unde.",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi Team,",
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Yesterday 10:33",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Sara Dechicco", cls="py-3 px-1 flex-1 truncate"),
                                Td("Thursday 09:22", cls="py-3 px-1 flex-1 truncate"),
                                Td("UK Support", cls="py-3 px-1 flex-1 truncate"),
                                Td("Nico Braun", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Th(
                                    H2(
                                        Span("Priority", cls="font-normal mr-1"),
                                        Span("Medium"),
                                        cls="text-sm",
                                    ),
                                    colspan="7",
                                    cls="bg-gray-100 text-left px-3 py-2 flex-1",
                                ),
                                cls="border-b flex",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "N",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-yellow-400 text-black leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "New",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-yellow-400 text-black",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Medium)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Excepturi at labore vel accusamus exercitationem\n                            assumenda ex incidunt eum quam, amet provident!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(cls="font-semibold"),
                                                        P(
                                                            cls="ml-auto text-gray-700 text-sm"
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(cls="mt-2"),
                                                    cls="mt-4 hidden",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "Excepturi at labore vel accusamus exercitationem assumenda\n                      ex incidunt eum quam, amet provident!",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "New",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-yellow-400 text-black",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Medium)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Excepturi at labore vel accusamus exercitationem\n                            assumenda ex incidunt eum quam, amet provident!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Odit consequatur natus aut reiciendis nisi\n                            sed! Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(cls="text-gray-600"),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(cls="font-semibold"),
                                                        P(
                                                            cls="ml-auto text-gray-700 text-sm"
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Dolore odio error inventore sint et dolorum\n                            asperiores exercitationem, quisquam esse tempora\n                            aliquam voluptates quibusdam quae debitis laboriosam\n                            iure ea quos.",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4 hidden",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Freddy Murro", cls="py-3 px-1 flex-1 truncate"),
                                Td("Today 12:13", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Td(
                                    Input(type="checkbox", cls="mt-1"),
                                    Div(
                                        Span(
                                            "O",
                                            style="\n                        padding: 2px 5px;\n                        font-size: 0.7rem;\n                        position: relative;\n                        bottom: 2px;\n                      ",
                                            cls="font-mono rounded-sm bg-red-600 text-white leading-none",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Medium)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Odit consequatur natus aut reiciendis nisi sed!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            aria_label="commenter",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Today 06:34",
                                                            aria_label="time",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Quos explicabo sed nisi totam dolores deleniti\n                            blanditiis culpa dolor provident perferendis\n                            sapiente corrupti repudiandae ea dolore.",
                                                        aria_label="comment",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="ml-auto relative group",
                                    ),
                                    role="cell",
                                    headers="select",
                                    cls="py-3 pl-3 pr-1 w-24 flex items-start",
                                ),
                                Td("#12534", cls="py-3 px-1 w-24"),
                                Td(
                                    Div(
                                        P(
                                            "Odit consequatur natus aut reiciendis nisi sed!",
                                            cls="w-full truncate",
                                        ),
                                        Span(
                                            Article(
                                                Header(
                                                    Div(
                                                        Span(
                                                            "Open",
                                                            cls="px-3 py-1 uppercase text-xs leading-none rounded-sm bg-red-600 text-white",
                                                        ),
                                                        Span(
                                                            "Incident #12534",
                                                            cls="ml-2 text-gray-700",
                                                        ),
                                                        Span("(Medium)", cls="ml-1"),
                                                    )
                                                ),
                                                Section(
                                                    H1(
                                                        "Odit consequatur natus aut reiciendis nisi sed!",
                                                        cls="text-sm font-semibold mt-3",
                                                    ),
                                                    P(
                                                        "Hi,",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur adipisicing\n                            elit. Error accusantium molestias fugit commodi\n                            doloremque.",
                                                        Br(),
                                                        Br(),
                                                        "Lorem ipsum dolor sit amet consectetur, adipisicing\n                            elit. Temporibus, quibusdam voluptates? ...",
                                                        cls="mt-3",
                                                    ),
                                                    cls="mt-5",
                                                ),
                                                Footer(
                                                    P(
                                                        "Latest Comments",
                                                        cls="text-gray-600",
                                                    ),
                                                    Hr(cls="mt-1"),
                                                    Div(
                                                        P(
                                                            "Nico Braun",
                                                            aria_label="commenter",
                                                            cls="font-semibold",
                                                        ),
                                                        P(
                                                            "Today 06:34",
                                                            aria_label="time",
                                                            cls="ml-auto text-gray-700 text-sm",
                                                        ),
                                                        cls="flex mt-3",
                                                    ),
                                                    P(
                                                        "Quos explicabo sed nisi totam dolores deleniti\n                            blanditiis culpa dolor provident perferendis\n                            sapiente corrupti repudiandae ea dolore.",
                                                        aria_label="comment",
                                                        cls="mt-2",
                                                    ),
                                                    cls="mt-4",
                                                ),
                                            ),
                                            cls="hidden group-hover:block ml-4 mt-10 w-screen max-w-lg absolute top-0 border shadow-lg p-6 bg-white rounded-md z-50 text-gray-900",
                                        ),
                                        cls="relative group w-full",
                                    ),
                                    cls="py-3 px-1 w-full max-w-xs xl:max-w-lg",
                                ),
                                Td("Carla Sandaers", cls="py-3 px-1 flex-1 truncate"),
                                Td("Today 08:13", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                Td("-", cls="py-3 px-1 flex-1 truncate"),
                                role="row",
                                cls="hover:bg-blue-100 border-b flex cursor-pointer",
                            ),
                            Tr(
                                Th(
                                    H2(
                                        Span("Priority", cls="font-normal mr-1"),
                                        Span("High"),
                                        cls="text-sm",
                                    ),
                                    colspan="7",
                                    cls="bg-gray-100 text-left px-3 py-2 flex-1",
                                ),
                                cls="border-b flex hidden",
                            ),
                            cls="flex w-full flex-col flex-1 min-h-0 overflow-hidden px-4",
                        ),
                        aria_describedby="info-popup",
                        aria_label="open tickets",
                        cls="border-t w-full min-h-0 h-full flex flex-col",
                    ),
                    Footer(
                        "footer",
                        aria_label="content footer",
                        cls="flex p-3 bg-white border-t hidden",
                    ),
                    aria_label="main content",
                    cls="flex min-h-0 flex-col flex-auto border-l",
                ),
                cls="flex-grow flex min-h-0 border-t",
            ),
            cls="flex-1 flex flex-col",
        ),
        cls="h-full w-full flex overflow-hidden antialiased text-gray-800 bg-white",
    ),
    cls="antialiased h-full",
)
