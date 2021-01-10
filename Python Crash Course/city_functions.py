def city_country(city, country, population=''):

    if population:
        full_text = f'{city.title()}, {country.title()} - population {population}'
    else:
        full_text = f'{city.title()}, {country.title()}'

    return full_text
