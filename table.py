from fasthtml.components import *

content = Div(
    Table(
        Thead(
            Tr(
                Th('Name', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Th('Date of Birth', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Th('Role', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Th('Salary', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900')
            ),
            cls='ltr:text-left rtl:text-right'
        ),
        Tbody(
            Tr(
                Td('John Doe', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Td('24/05/1995', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('Web Developer', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('$120,000', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                cls='odd:bg-gray-50'
            ),
            Tr(
                Td('Jane Doe', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Td('04/11/1980', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('Web Designer', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('$100,000', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                cls='odd:bg-gray-50'
            ),
            Tr(
                Td('Gary Barlow', cls='whitespace-nowrap px-4 py-2 font-medium text-gray-900'),
                Td('24/05/1995', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('Singer', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                Td('$20,000', cls='whitespace-nowrap px-4 py-2 text-gray-700'),
                cls='odd:bg-gray-50'
            ),
            cls='divide-y divide-gray-200'
        ),
        cls='min-w-full divide-y-2 divide-gray-200 bg-white text-sm'
    ),
    cls='overflow-x-auto'
)