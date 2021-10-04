capitals = {
  "Porto Velho": "Norte",
  "Manaus": "Norte",
  "Rio Branco": "Norte",
  "Campo Grande": "Centro-oeste",
  "Macapá": "Norte",
  "Brasília": "Centro-oeste",
  "Boa Vista": "Norte",
  "Cuiabá": "Centro-oeste",
  "Palmas": "Norte",
  "São Paulo": "Sudeste",
  "Teresina": "Nordeste",
  "Rio de Janeiro": "Sudeste",
  "Belém": "Norte",
  "Goiânia": "Centro-oeste",
  "Salvador": "Nordeste",
  "Florianópolis": "Sul",
  "São Luís": "Nordeste",
  "Maceió": "Nordeste",
  "Porto Alegre": "Sul",
  "Curitiba": "Sul",
  "Belo Horizonte": "Sudeste",
  "Fortaleza": "Nordeste",
  "Recife": "Nordeste",
  "João Pessoa": "Nordeste",
  "Aracaju": "Nordeste",
  "Natal": "Nordeste",
  "Vitória": "Sudeste",
}

# [“Rio Branco”,”Macapá”], [“Macapá”,”Manaus”], [“Belém”,”Porto Velho”], [“Boa
# Vista”,”Palmas”], [“Belém”,”Rio Branco”], [“Palmas”,”Rio Branco”], [“Boa
# Vista”,”Salvador”], [“Maceió”,”Fortaleza”], [“São Luís”,”Salvador”], [“João
# Pessoa”,”Recife”], [“Recife”,”Teresina”], [“Teresina”,”Natal”], [“Aracaju”,”Salvador”],
# [“Natal”,”Aracaju”], [“Goiânia”,”Cuiabá”], [“Cuiabá”,”Campo Grande”], [“Campo
# Grande”,”Brasília”], [“Vitória”, “Cuiabá”], [“Vitória”,”Belo Horizonte”], [“Belo
# Horizonte”,”São Paulo”], [“São Paulo”,”Rio de Janeiro”], [“Rio de Janeiro”,”Curitiba”],
# [“Curitiba”,”Florianópolis”], [“Florianópolis”,”Porto Alegre”]

routes = [
  ("Boa Vista", "Salvador"),
  ("Vitória", "Cuiabá"),
  ("Rio de Janeiro", "Curitiba"),
  ("Rio Branco", "Macapá")
]

def identify_interregional_routes(routes):
    interregional_routes = set()
    for origin, destiny in routes:
        if capitals[origin] != capitals[destiny]:
            interregional_routes.add((capitals[origin], capitals[destiny]))
    return interregional_routes

interregional_routes = identify_interregional_routes(routes)

# falta uma função para tratar o "interregional_routes"
# para evitar criar rotas desnecessárias
def identify_routes_to_add(interregional_routes):
    route_to_add = []
    routes = list(interregional_routes)
    for index in range(len(routes)):
        route_to_add.append((routes[index][1], routes[(index+1) % len(routes)][0]))
    print(f"Quantidade de rotas: {len(route_to_add)}")
    print(route_to_add)

identify_routes_to_add(interregional_routes)
