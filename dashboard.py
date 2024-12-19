from fasthtml.components import *
from fasthtml.svg import *

content = Div(
    Aside(
        Div(
            A(
                H6('Material Tailwind Dashboard', cls='block antialiased tracking-normal font-sans text-base font-semibold leading-relaxed text-white'),
                href='#/',
                cls='flex items-center gap-4 py-6 px-8'
            ),
            Button(
                Span(
                    Svg(
                        Path(stroke_linecap='round', stroke_linejoin='round', d='M6 18L18 6M6 6l12 12'),
                        xmlns='http://www.w3.org/2000/svg',
                        fill='none',
                        viewbox='0 0 24 24',
                        stroke_width='2.5',
                        stroke='currentColor',
                        aria_hidden='true',
                        cls='h-5 w-5 text-white'
                    ),
                    cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                ),
                type='button',
                cls='middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-8 max-w-[32px] h-8 max-h-[32px] rounded-lg text-xs text-white hover:bg-white/10 active:bg-white/30 absolute right-0 top-0 grid rounded-br-none rounded-tl-none xl:hidden'
            ),
            cls='relative border-b border-white/20'
        ),
        Div(
            Ul(
                Li(
                    A(
                        Button(
                            Svg(
                                Path(d='M11.47 3.84a.75.75 0 011.06 0l8.69 8.69a.75.75 0 101.06-1.06l-8.689-8.69a2.25 2.25 0 00-3.182 0l-8.69 8.69a.75.75 0 001.061 1.06l8.69-8.69z'),
                                Path(d='M12 5.432l8.159 8.159c.03.03.06.058.091.086v6.198c0 1.035-.84 1.875-1.875 1.875H15a.75.75 0 01-.75-.75v-4.5a.75.75 0 00-.75-.75h-3a.75.75 0 00-.75.75V21a.75.75 0 01-.75.75H5.625a1.875 1.875 0 01-1.875-1.875v-6.198a2.29 2.29 0 00.091-.086L12 5.43z'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('dashboard', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-md shadow-blue-500/20 hover:shadow-lg hover:shadow-blue-500/40 active:opacity-[0.85] w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        aria_current='page',
                        href='#',
                        cls='active'
                    )
                ),
                Li(
                    A(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M18.685 19.097A9.723 9.723 0 0021.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 003.065 7.097A9.716 9.716 0 0012 21.75a9.716 9.716 0 006.685-2.653zm-12.54-1.285A7.486 7.486 0 0112 15a7.486 7.486 0 015.855 2.812A8.224 8.224 0 0112 20.25a8.224 8.224 0 01-5.855-2.438zM15.75 9a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('profile', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-white hover:bg-white/10 active:bg-white/30 w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        href='#',
                        cls=True
                    )
                ),
                Li(
                    A(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M1.5 5.625c0-1.036.84-1.875 1.875-1.875h17.25c1.035 0 1.875.84 1.875 1.875v12.75c0 1.035-.84 1.875-1.875 1.875H3.375A1.875 1.875 0 011.5 18.375V5.625zM21 9.375A.375.375 0 0020.625 9h-7.5a.375.375 0 00-.375.375v1.5c0 .207.168.375.375.375h7.5a.375.375 0 00.375-.375v-1.5zm0 3.75a.375.375 0 00-.375-.375h-7.5a.375.375 0 00-.375.375v1.5c0 .207.168.375.375.375h7.5a.375.375 0 00.375-.375v-1.5zm0 3.75a.375.375 0 00-.375-.375h-7.5a.375.375 0 00-.375.375v1.5c0 .207.168.375.375.375h7.5a.375.375 0 00.375-.375v-1.5zM10.875 18.75a.375.375 0 00.375-.375v-1.5a.375.375 0 00-.375-.375h-7.5a.375.375 0 00-.375.375v1.5c0 .207.168.375.375.375h7.5zM3.375 15h7.5a.375.375 0 00.375-.375v-1.5a.375.375 0 00-.375-.375h-7.5a.375.375 0 00-.375.375v1.5c0 .207.168.375.375.375zm0-3.75h7.5a.375.375 0 00.375-.375v-1.5A.375.375 0 0010.875 9h-7.5A.375.375 0 003 9.375v1.5c0 .207.168.375.375.375z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('tables', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-white hover:bg-white/10 active:bg-white/30 w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        href='#',
                        cls=True
                    )
                ),
                Li(
                    A(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M5.25 9a6.75 6.75 0 0113.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 01-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 11-7.48 0 24.585 24.585 0 01-4.831-1.244.75.75 0 01-.298-1.205A8.217 8.217 0 005.25 9.75V9zm4.502 8.9a2.25 2.25 0 104.496 0 25.057 25.057 0 01-4.496 0z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('notifactions', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-white hover:bg-white/10 active:bg-white/30 w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        href='#',
                        cls=True
                    )
                ),
                cls='mb-4 flex flex-col gap-1'
            ),
            Ul(
                Li(
                    P('auth pages', cls='block antialiased font-sans text-sm leading-normal text-white font-black uppercase opacity-75'),
                    cls='mx-3.5 mt-4 mb-2'
                ),
                Li(
                    A(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M7.5 3.75A1.5 1.5 0 006 5.25v13.5a1.5 1.5 0 001.5 1.5h6a1.5 1.5 0 001.5-1.5V15a.75.75 0 011.5 0v3.75a3 3 0 01-3 3h-6a3 3 0 01-3-3V5.25a3 3 0 013-3h6a3 3 0 013 3V9A.75.75 0 0115 9V5.25a1.5 1.5 0 00-1.5-1.5h-6zm10.72 4.72a.75.75 0 011.06 0l3 3a.75.75 0 010 1.06l-3 3a.75.75 0 11-1.06-1.06l1.72-1.72H9a.75.75 0 010-1.5h10.94l-1.72-1.72a.75.75 0 010-1.06z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('sign in', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-white hover:bg-white/10 active:bg-white/30 w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        href='#',
                        cls=True
                    )
                ),
                Li(
                    A(
                        Button(
                            Svg(
                                Path(d='M6.25 6.375a4.125 4.125 0 118.25 0 4.125 4.125 0 01-8.25 0zM3.25 19.125a7.125 7.125 0 0114.25 0v.003l-.001.119a.75.75 0 01-.363.63 13.067 13.067 0 01-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 01-.364-.63l-.001-.122zM19.75 7.5a.75.75 0 00-1.5 0v2.25H16a.75.75 0 000 1.5h2.25v2.25a.75.75 0 001.5 0v-2.25H22a.75.75 0 000-1.5h-2.25V7.5z'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='w-5 h-5 text-inherit'
                            ),
                            P('sign up', cls='block antialiased font-sans text-base leading-relaxed text-inherit font-medium capitalize'),
                            type='button',
                            cls='middle none font-sans font-bold center transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-white hover:bg-white/10 active:bg-white/30 w-full flex items-center gap-4 px-4 capitalize'
                        ),
                        href='#',
                        cls=True
                    )
                ),
                cls='mb-4 flex flex-col gap-1'
            ),
            cls='m-4'
        ),
        cls='bg-gradient-to-br from-gray-800 to-gray-900 -translate-x-80 fixed inset-0 z-50 my-4 ml-4 h-[calc(100vh-32px)] w-72 rounded-xl transition-transform duration-300 xl:translate-x-0'
    ),
    Div(
        Nav(
            Div(
                Div(
                    Nav(
                        Ol(
                            Li(
                                A(
                                    P('dashboard', cls='block antialiased font-sans text-sm leading-normal text-blue-900 font-normal opacity-50 transition-all hover:text-blue-500 hover:opacity-100'),
                                    href='#'
                                ),
                                Span('/', cls='text-gray-500 text-sm antialiased font-sans font-normal leading-normal mx-2 pointer-events-none select-none'),
                                cls='flex items-center text-blue-gray-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-light-blue-500'
                            ),
                            Li(
                                P('home', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-normal'),
                                cls='flex items-center text-blue-900 antialiased font-sans text-sm font-normal leading-normal cursor-pointer transition-colors duration-300 hover:text-blue-500'
                            ),
                            cls='flex flex-wrap items-center w-full bg-opacity-60 rounded-md bg-transparent p-0 transition-all'
                        ),
                        aria_label='breadcrumb',
                        cls='w-max'
                    ),
                    H6('home', cls='block antialiased tracking-normal font-sans text-base font-semibold leading-relaxed text-gray-900'),
                    cls='capitalize'
                ),
                Div(
                    Div(
                        Div(
                            Input(placeholder=' ', cls='peer w-full h-full bg-transparent text-gray-700 font-sans font-normal outline outline-0 focus:outline-0 disabled:bg-blue-gray-50 disabled:border-0 transition-all placeholder-shown:border placeholder-shown:border-blue-gray-200 placeholder-shown:border-t-blue-gray-200 border focus:border-2 border-t-transparent focus:border-t-transparent text-sm px-3 py-2.5 rounded-[7px] border-blue-gray-200 focus:border-blue-500'),
                            Label('Type here', cls="flex w-full h-full select-none pointer-events-none absolute left-0 font-normal peer-placeholder-shown:text-gray-500 leading-tight peer-focus:leading-tight peer-disabled:text-transparent peer-disabled:peer-placeholder-shown:text-blue-gray-500 transition-all -top-1.5 peer-placeholder-shown:text-sm text-[11px] peer-focus:text-[11px] before:content[' '] before:block before:box-border before:w-2.5 before:h-1.5 before:mt-[6.5px] before:mr-1 peer-placeholder-shown:before:border-transparent before:rounded-tl-md before:border-t peer-focus:before:border-t-2 before:border-l peer-focus:before:border-l-2 before:pointer-events-none before:transition-all peer-disabled:before:border-transparent after:content[' '] after:block after:flex-grow after:box-border after:w-2.5 after:h-1.5 after:mt-[6.5px] after:ml-1 peer-placeholder-shown:after:border-transparent after:rounded-tr-md after:border-t peer-focus:after:border-t-2 after:border-r peer-focus:after:border-r-2 after:pointer-events-none after:transition-all peer-disabled:after:border-transparent peer-placeholder-shown:leading-[3.75] text-blue-gray-400 peer-focus:text-blue-500 before:border-blue-gray-200 peer-focus:before:border-blue-500 after:border-blue-gray-200 peer-focus:after:border-blue-500"),
                            cls='relative w-full min-w-[200px] h-10'
                        ),
                        cls='mr-auto md:mr-4 md:w-56'
                    ),
                    Button(
                        Span(
                            Svg(
                                Path(fill_rule='evenodd', d='M3 6.75A.75.75 0 013.75 6h16.5a.75.75 0 010 1.5H3.75A.75.75 0 013 6.75zM3 12a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75A.75.75 0 013 12zm0 5.25a.75.75 0 01.75-.75h16.5a.75.75 0 010 1.5H3.75a.75.75 0 01-.75-.75z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                stroke_width='3',
                                cls='h-6 w-6 text-blue-gray-500'
                            ),
                            cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                        ),
                        type='button',
                        cls='relative middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-10 max-w-[40px] h-10 max-h-[40px] rounded-lg text-xs text-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 grid xl:hidden'
                    ),
                    A(
                        Button(
                            Svg(
                                Path(fill_rule='evenodd', d='M18.685 19.097A9.723 9.723 0 0021.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 003.065 7.097A9.716 9.716 0 0012 21.75a9.716 9.716 0 006.685-2.653zm-12.54-1.285A7.486 7.486 0 0112 15a7.486 7.486 0 015.855 2.812A8.224 8.224 0 0112 20.25a8.224 8.224 0 01-5.855-2.438zM15.75 9a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='h-5 w-5 text-blue-gray-500'
                            ),
                            'Sign In',
                            type='button',
                            cls='middle none font-sans font-bold center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none text-xs py-3 rounded-lg text-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 hidden items-center gap-1 px-4 xl:flex'
                        ),
                        Button(
                            Span(
                                Svg(
                                    Path(fill_rule='evenodd', d='M18.685 19.097A9.723 9.723 0 0021.75 12c0-5.385-4.365-9.75-9.75-9.75S2.25 6.615 2.25 12a9.723 9.723 0 003.065 7.097A9.716 9.716 0 0012 21.75a9.716 9.716 0 006.685-2.653zm-12.54-1.285A7.486 7.486 0 0112 15a7.486 7.486 0 015.855 2.812A8.224 8.224 0 0112 20.25a8.224 8.224 0 01-5.855-2.438zM15.75 9a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0z', clip_rule='evenodd'),
                                    xmlns='http://www.w3.org/2000/svg',
                                    viewbox='0 0 24 24',
                                    fill='currentColor',
                                    aria_hidden='true',
                                    cls='h-5 w-5 text-blue-gray-500'
                                ),
                                cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                            ),
                            type='button',
                            cls='relative middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-10 max-w-[40px] h-10 max-h-[40px] rounded-lg text-xs text-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30 grid xl:hidden'
                        ),
                        href='#'
                    ),
                    Button(
                        Span(
                            Svg(
                                Path(fill_rule='evenodd', d='M11.078 2.25c-.917 0-1.699.663-1.85 1.567L9.05 4.889c-.02.12-.115.26-.297.348a7.493 7.493 0 00-.986.57c-.166.115-.334.126-.45.083L6.3 5.508a1.875 1.875 0 00-2.282.819l-.922 1.597a1.875 1.875 0 00.432 2.385l.84.692c.095.078.17.229.154.43a7.598 7.598 0 000 1.139c.015.2-.059.352-.153.43l-.841.692a1.875 1.875 0 00-.432 2.385l.922 1.597a1.875 1.875 0 002.282.818l1.019-.382c.115-.043.283-.031.45.082.312.214.641.405.985.57.182.088.277.228.297.35l.178 1.071c.151.904.933 1.567 1.85 1.567h1.844c.916 0 1.699-.663 1.85-1.567l.178-1.072c.02-.12.114-.26.297-.349.344-.165.673-.356.985-.57.167-.114.335-.125.45-.082l1.02.382a1.875 1.875 0 002.28-.819l.923-1.597a1.875 1.875 0 00-.432-2.385l-.84-.692c-.095-.078-.17-.229-.154-.43a7.614 7.614 0 000-1.139c-.016-.2.059-.352.153-.43l.84-.692c.708-.582.891-1.59.433-2.385l-.922-1.597a1.875 1.875 0 00-2.282-.818l-1.02.382c-.114.043-.282.031-.449-.083a7.49 7.49 0 00-.985-.57c-.183-.087-.277-.227-.297-.348l-.179-1.072a1.875 1.875 0 00-1.85-1.567h-1.843zM12 15.75a3.75 3.75 0 100-7.5 3.75 3.75 0 000 7.5z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='h-5 w-5 text-blue-gray-500'
                            ),
                            cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                        ),
                        type='button',
                        cls='relative middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-10 max-w-[40px] h-10 max-h-[40px] rounded-lg text-xs text-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30'
                    ),
                    Button(
                        Span(
                            Svg(
                                Path(fill_rule='evenodd', d='M5.25 9a6.75 6.75 0 0113.5 0v.75c0 2.123.8 4.057 2.118 5.52a.75.75 0 01-.297 1.206c-1.544.57-3.16.99-4.831 1.243a3.75 3.75 0 11-7.48 0 24.585 24.585 0 01-4.831-1.244.75.75 0 01-.298-1.205A8.217 8.217 0 005.25 9.75V9zm4.502 8.9a2.25 2.25 0 104.496 0 25.057 25.057 0 01-4.496 0z', clip_rule='evenodd'),
                                xmlns='http://www.w3.org/2000/svg',
                                viewbox='0 0 24 24',
                                fill='currentColor',
                                aria_hidden='true',
                                cls='h-5 w-5 text-blue-gray-500'
                            ),
                            cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                        ),
                        aria_expanded='false',
                        aria_haspopup='menu',
                        id=':r2:',
                        type='button',
                        cls='relative middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-10 max-w-[40px] h-10 max-h-[40px] rounded-lg text-xs text-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30'
                    ),
                    cls='flex items-center'
                ),
                cls='flex flex-col-reverse justify-between gap-6 md:flex-row md:items-center'
            ),
            cls='block w-full max-w-full bg-transparent text-white shadow-none rounded-xl transition-all px-0 py-1'
        ),
        Div(
            Div(
                Div(
                    Div(
                        Svg(
                            Path(d='M12 7.5a2.25 2.25 0 100 4.5 2.25 2.25 0 000-4.5z'),
                            Path(fill_rule='evenodd', d='M1.5 4.875C1.5 3.839 2.34 3 3.375 3h17.25c1.035 0 1.875.84 1.875 1.875v9.75c0 1.036-.84 1.875-1.875 1.875H3.375A1.875 1.875 0 011.5 14.625v-9.75zM8.25 9.75a3.75 3.75 0 117.5 0 3.75 3.75 0 01-7.5 0zM18.75 9a.75.75 0 00-.75.75v.008c0 .414.336.75.75.75h.008a.75.75 0 00.75-.75V9.75a.75.75 0 00-.75-.75h-.008zM4.5 9.75A.75.75 0 015.25 9h.008a.75.75 0 01.75.75v.008a.75.75 0 01-.75.75H5.25a.75.75 0 01-.75-.75V9.75z', clip_rule='evenodd'),
                            Path(d='M2.25 18a.75.75 0 000 1.5c5.4 0 10.63.722 15.6 2.075 1.19.324 2.4-.558 2.4-1.82V18.75a.75.75 0 00-.75-.75H2.25z'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            fill='currentColor',
                            aria_hidden='true',
                            cls='w-6 h-6 text-white'
                        ),
                        cls='bg-clip-border mx-4 rounded-xl overflow-hidden bg-gradient-to-tr from-blue-600 to-blue-400 text-white shadow-blue-500/40 shadow-lg absolute -mt-4 grid h-16 w-16 place-items-center'
                    ),
                    Div(
                        P("Today's Money", cls='block antialiased font-sans text-sm leading-normal font-normal text-blue-gray-600'),
                        H4('$53k', cls='block antialiased tracking-normal font-sans text-2xl font-semibold leading-snug text-blue-gray-900'),
                        cls='p-4 text-right'
                    ),
                    Div(
                        P(
                            Strong('+55%', cls='text-green-500'),
                            'than last week',
                            cls='block antialiased font-sans text-base leading-relaxed font-normal text-blue-gray-600'
                        ),
                        cls='border-t border-blue-gray-50 p-4'
                    ),
                    cls='relative flex flex-col bg-clip-border rounded-xl bg-white text-gray-700 shadow-md'
                ),
                Div(
                    Div(
                        Svg(
                            Path(fill_rule='evenodd', d='M7.5 6a4.5 4.5 0 119 0 4.5 4.5 0 01-9 0zM3.751 20.105a8.25 8.25 0 0116.498 0 .75.75 0 01-.437.695A18.683 18.683 0 0112 22.5c-2.786 0-5.433-.608-7.812-1.7a.75.75 0 01-.437-.695z', clip_rule='evenodd'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            fill='currentColor',
                            aria_hidden='true',
                            cls='w-6 h-6 text-white'
                        ),
                        cls='bg-clip-border mx-4 rounded-xl overflow-hidden bg-gradient-to-tr from-pink-600 to-pink-400 text-white shadow-pink-500/40 shadow-lg absolute -mt-4 grid h-16 w-16 place-items-center'
                    ),
                    Div(
                        P("Today's Users", cls='block antialiased font-sans text-sm leading-normal font-normal text-blue-gray-600'),
                        H4('2,300', cls='block antialiased tracking-normal font-sans text-2xl font-semibold leading-snug text-blue-gray-900'),
                        cls='p-4 text-right'
                    ),
                    Div(
                        P(
                            Strong('+3%', cls='text-green-500'),
                            'than last month',
                            cls='block antialiased font-sans text-base leading-relaxed font-normal text-blue-gray-600'
                        ),
                        cls='border-t border-blue-gray-50 p-4'
                    ),
                    cls='relative flex flex-col bg-clip-border rounded-xl bg-white text-gray-700 shadow-md'
                ),
                Div(
                    Div(
                        Svg(
                            Path(d='M6.25 6.375a4.125 4.125 0 118.25 0 4.125 4.125 0 01-8.25 0zM3.25 19.125a7.125 7.125 0 0114.25 0v.003l-.001.119a.75.75 0 01-.363.63 13.067 13.067 0 01-6.761 1.873c-2.472 0-4.786-.684-6.76-1.873a.75.75 0 01-.364-.63l-.001-.122zM19.75 7.5a.75.75 0 00-1.5 0v2.25H16a.75.75 0 000 1.5h2.25v2.25a.75.75 0 001.5 0v-2.25H22a.75.75 0 000-1.5h-2.25V7.5z'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            fill='currentColor',
                            aria_hidden='true',
                            cls='w-6 h-6 text-white'
                        ),
                        cls='bg-clip-border mx-4 rounded-xl overflow-hidden bg-gradient-to-tr from-green-600 to-green-400 text-white shadow-green-500/40 shadow-lg absolute -mt-4 grid h-16 w-16 place-items-center'
                    ),
                    Div(
                        P('New Clients', cls='block antialiased font-sans text-sm leading-normal font-normal text-blue-gray-600'),
                        H4('3,462', cls='block antialiased tracking-normal font-sans text-2xl font-semibold leading-snug text-blue-gray-900'),
                        cls='p-4 text-right'
                    ),
                    Div(
                        P(
                            Strong('-2%', cls='text-red-500'),
                            'than yesterday',
                            cls='block antialiased font-sans text-base leading-relaxed font-normal text-blue-gray-600'
                        ),
                        cls='border-t border-blue-gray-50 p-4'
                    ),
                    cls='relative flex flex-col bg-clip-border rounded-xl bg-white text-gray-700 shadow-md'
                ),
                Div(
                    Div(
                        Svg(
                            Path(d='M18.375 2.25c-1.035 0-1.875.84-1.875 1.875v15.75c0 1.035.84 1.875 1.875 1.875h.75c1.035 0 1.875-.84 1.875-1.875V4.125c0-1.036-.84-1.875-1.875-1.875h-.75zM9.75 8.625c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v11.25c0 1.035-.84 1.875-1.875 1.875h-.75a1.875 1.875 0 01-1.875-1.875V8.625zM3 13.125c0-1.036.84-1.875 1.875-1.875h.75c1.036 0 1.875.84 1.875 1.875v6.75c0 1.035-.84 1.875-1.875 1.875h-.75A1.875 1.875 0 013 19.875v-6.75z'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            fill='currentColor',
                            aria_hidden='true',
                            cls='w-6 h-6 text-white'
                        ),
                        cls='bg-clip-border mx-4 rounded-xl overflow-hidden bg-gradient-to-tr from-orange-600 to-orange-400 text-white shadow-orange-500/40 shadow-lg absolute -mt-4 grid h-16 w-16 place-items-center'
                    ),
                    Div(
                        P('Sales', cls='block antialiased font-sans text-sm leading-normal font-normal text-blue-gray-600'),
                        H4('$103,430', cls='block antialiased tracking-normal font-sans text-2xl font-semibold leading-snug text-blue-gray-900'),
                        cls='p-4 text-right'
                    ),
                    Div(
                        P(
                            Strong('+5%', cls='text-green-500'),
                            'than yesterday',
                            cls='block antialiased font-sans text-base leading-relaxed font-normal text-blue-gray-600'
                        ),
                        cls='border-t border-blue-gray-50 p-4'
                    ),
                    cls='relative flex flex-col bg-clip-border rounded-xl bg-white text-gray-700 shadow-md'
                ),
                cls='mb-12 grid gap-y-10 gap-x-6 md:grid-cols-2 xl:grid-cols-4'
            ),
            Div(
                Div(
                    Div(
                        Div(
                            H6('Projects', cls='block antialiased tracking-normal font-sans text-base font-semibold leading-relaxed text-blue-gray-900 mb-1'),
                            P(
                                Svg(
                                    Path(stroke_linecap='round', stroke_linejoin='round', d='M4.5 12.75l6 6 9-13.5'),
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='none',
                                    viewbox='0 0 24 24',
                                    stroke_width='3',
                                    stroke='currentColor',
                                    aria_hidden='true',
                                    cls='h-4 w-4 text-blue-500'
                                ),
                                Strong('30 done'),
                                'this month',
                                cls='antialiased font-sans text-sm leading-normal flex items-center gap-1 font-normal text-blue-gray-600'
                            )
                        ),
                        Button(
                            Span(
                                Svg(
                                    Path(stroke_linecap='round', stroke_linejoin='round', d='M12 6.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 12.75a.75.75 0 110-1.5.75.75 0 010 1.5zM12 18.75a.75.75 0 110-1.5.75.75 0 010 1.5z'),
                                    xmlns='http://www.w3.org/2000/svg',
                                    fill='currenColor',
                                    viewbox='0 0 24 24',
                                    stroke_width='3',
                                    stroke='currentColor',
                                    aria_hidden='true',
                                    cls='h-6 w-6'
                                ),
                                cls='absolute top-1/2 left-1/2 transform -translate-y-1/2 -translate-x-1/2'
                            ),
                            aria_expanded='false',
                            aria_haspopup='menu',
                            id=':r5:',
                            type='button',
                            cls='relative middle none font-sans font-medium text-center uppercase transition-all disabled:opacity-50 disabled:shadow-none disabled:pointer-events-none w-8 max-w-[32px] h-8 max-h-[32px] rounded-lg text-xs text-blue-gray-500 hover:bg-blue-gray-500/10 active:bg-blue-gray-500/30'
                        ),
                        cls='relative bg-clip-border rounded-xl overflow-hidden bg-transparent text-gray-700 shadow-none m-0 flex items-center justify-between p-6'
                    ),
                    Div(
                        Table(
                            Thead(
                                Tr(
                                    Th(
                                        P('companies', cls='block antialiased font-sans text-[11px] font-medium uppercase text-blue-gray-400'),
                                        cls='border-b border-blue-gray-50 py-3 px-6 text-left'
                                    ),
                                    Th(
                                        P('budget', cls='block antialiased font-sans text-[11px] font-medium uppercase text-blue-gray-400'),
                                        cls='border-b border-blue-gray-50 py-3 px-6 text-left'
                                    ),
                                    Th(
                                        P('completion', cls='block antialiased font-sans text-[11px] font-medium uppercase text-blue-gray-400'),
                                        cls='border-b border-blue-gray-50 py-3 px-6 text-left'
                                    )
                                )
                            ),
                            Tbody(
                                Tr(
                                    Td(
                                        Div(
                                            P('Material XD Version', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-bold'),
                                            cls='flex items-center gap-4'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        P('$14,000', cls='block antialiased font-sans text-xs font-medium text-blue-gray-600'),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        Div(
                                            P('60%', cls='antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600'),
                                            Div(
                                                Div(style='width: 60%', cls='flex justify-center items-center h-full bg-gradient-to-tr from-blue-600 to-blue-400 text-white'),
                                                cls='flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1'
                                            ),
                                            cls='w-10/12'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    )
                                ),
                                Tr(
                                    Td(
                                        Div(
                                            P('Add Progress Track', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-bold'),
                                            cls='flex items-center gap-4'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        P('$3,000', cls='block antialiased font-sans text-xs font-medium text-blue-gray-600'),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        Div(
                                            P('10%', cls='antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600'),
                                            Div(
                                                Div(style='width: 10%', cls='flex justify-center items-center h-full bg-gradient-to-tr from-blue-600 to-blue-400 text-white'),
                                                cls='flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1'
                                            ),
                                            cls='w-10/12'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    )
                                ),
                                Tr(
                                    Td(
                                        Div(
                                            P('Fix Platform Errors', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-bold'),
                                            cls='flex items-center gap-4'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        P('Not set', cls='block antialiased font-sans text-xs font-medium text-blue-gray-600'),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        Div(
                                            P('100%', cls='antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600'),
                                            Div(
                                                Div(style='width: 100%', cls='flex justify-center items-center h-full bg-gradient-to-tr from-green-600 to-green-400 text-white'),
                                                cls='flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1'
                                            ),
                                            cls='w-10/12'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    )
                                ),
                                Tr(
                                    Td(
                                        Div(
                                            P('Launch our Mobile App', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-bold'),
                                            cls='flex items-center gap-4'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        P('$20,500', cls='block antialiased font-sans text-xs font-medium text-blue-gray-600'),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        Div(
                                            P('100%', cls='antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600'),
                                            Div(
                                                Div(style='width: 100%', cls='flex justify-center items-center h-full bg-gradient-to-tr from-green-600 to-green-400 text-white'),
                                                cls='flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1'
                                            ),
                                            cls='w-10/12'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    )
                                ),
                                Tr(
                                    Td(
                                        Div(
                                            P('Add the New Pricing Page', cls='block antialiased font-sans text-sm leading-normal text-blue-gray-900 font-bold'),
                                            cls='flex items-center gap-4'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        P('$500', cls='block antialiased font-sans text-xs font-medium text-blue-gray-600'),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    ),
                                    Td(
                                        Div(
                                            P('25%', cls='antialiased font-sans mb-1 block text-xs font-medium text-blue-gray-600'),
                                            Div(
                                                Div(style='width: 25%', cls='flex justify-center items-center h-full bg-gradient-to-tr from-blue-600 to-blue-400 text-white'),
                                                cls='flex flex-start bg-blue-gray-50 overflow-hidden w-full rounded-sm font-sans text-xs font-medium h-1'
                                            ),
                                            cls='w-10/12'
                                        ),
                                        cls='py-3 px-5 border-b border-blue-gray-50'
                                    )
                                )
                            ),
                            cls='w-full min-w-[640px] table-auto'
                        ),
                        cls='p-6 overflow-x-scroll px-0 pt-0 pb-2'
                    ),
                    cls='relative flex flex-col bg-clip-border rounded-xl bg-white text-gray-700 shadow-md overflow-hidden xl:col-span-2'
                ),
                cls='mb-4 grid grid-cols-1 gap-6 xl:grid-cols-3'
            ),
            cls='mt-12'
        ),
        Div(
            Footer(
                Div(
                    P(
                        '© 2023, made with',
                        Svg(
                            Path(d='M11.645 20.91l-.007-.003-.022-.012a15.247 15.247 0 01-.383-.218 25.18 25.18 0 01-4.244-3.17C4.688 15.36 2.25 12.174 2.25 8.25 2.25 5.322 4.714 3 7.688 3A5.5 5.5 0 0112 5.052 5.5 5.5 0 0116.313 3c2.973 0 5.437 2.322 5.437 5.25 0 3.925-2.438 7.111-4.739 9.256a25.175 25.175 0 01-4.244 3.17 15.247 15.247 0 01-.383.219l-.022.012-.007.004-.003.001a.752.752 0 01-.704 0l-.003-.001z'),
                            xmlns='http://www.w3.org/2000/svg',
                            viewbox='0 0 24 24',
                            fill='currentColor',
                            aria_hidden='true',
                            cls='-mt-0.5 inline-block h-3.5 w-3.5'
                        ),
                        'by',
                        A('Creative Tim', href='https://www.creative-tim.com', target='_blank', cls='transition-colors hover:text-blue-500'),
                        'for a better web.',
                        cls='block antialiased font-sans text-sm leading-normal font-normal text-inherit'
                    ),
                    Ul(
                        Li(
                            A('Creative Tim', href='https://www.creative-tim.com', target='_blank', cls='block antialiased font-sans text-sm leading-normal py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500')
                        ),
                        Li(
                            A('About Us', href='https://www.creative-tim.com/presentation', target='_blank', cls='block antialiased font-sans text-sm leading-normal py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500')
                        ),
                        Li(
                            A('Blog', href='https://www.creative-tim.com/blog', target='_blank', cls='block antialiased font-sans text-sm leading-normal py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500')
                        ),
                        Li(
                            A('License', href='https://www.creative-tim.com/license', target='_blank', cls='block antialiased font-sans text-sm leading-normal py-0.5 px-1 font-normal text-inherit transition-colors hover:text-blue-500')
                        ),
                        cls='flex items-center gap-4'
                    ),
                    cls='flex w-full flex-wrap items-center justify-center gap-6 px-2 md:justify-between'
                ),
                cls='py-2'
            ),
            cls='text-blue-gray-600'
        ),
        cls='p-4 xl:ml-80'
    ),
    cls='min-h-screen bg-gray-50/50'
)