import json
from pathlib import Path
from pipeline.consolidate import _source, cache_file
from pipeline.pages import list_pages
from pipeline.store import read_json
from pipeline.config import CLUSTERS_FILE

RECIPES_DIR = Path("cache/recipes")
RECIPES_DIR.mkdir(parents=True, exist_ok=True)

clusters = {c["id"]: c for c in read_json(CLUSTERS_FILE)}
pages_by_label = {p.label: p for p in list_pages()}

def get_digest(cluster_id):
    c = clusters[cluster_id]
    _, digest = _source(c, pages_by_label)
    return digest

recipes = {}

# 1. Update 31#2
recipes["31#2"] = {
    "cluster": "31#2",
    "kind": "recipe",
    "source_refs": ["31#2", "256#1"],
    "source_hash": get_digest("31#2"),
    "recipe": {
        "title": "Azucarado de mantequilla",
        "category": "Básicos y rellenos",
        "tags": ["sin horno", "vegetariano"],
        "servings": "",
        "prep_time": "",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "Versión 1 libra (pág. 256)",
                "items": [
                    "4 onzas de margarina",
                    "1 pizca de sal",
                    "1 libra de azúcar glass cernida",
                    "2 yemas de huevo",
                    "1 cucharadita de vainilla",
                    "2 cucharadas de leche caliente"
                ]
            },
            {
                "name": "Versión 3 libras para decoración amplia (pág. 31)",
                "items": [
                    "12 onzas de mantequilla o margarina",
                    "3 libras de azúcar glass cernida",
                    "2 yemas de huevo",
                    "1 cucharada de vainilla",
                    "Colorantes vegetales (opcional)"
                ]
            }
        ],
        "steps": [
            "Cremar la margarina con la sal y agregar alternando con la leche el azúcar glass cernida.",
            "Por último se agregan las yemas y la vainilla batiendo a que quede suave y consistente para decorar."
        ],
        "teacher_notes": [
            "Las yemas le brindan una emulsión más estable y una textura aterciopelada que facilita trazar decoraciones."
        ],
        "notes": [
            "Este betún se puede pintar y sirve tanto para cubrir como para decorar pasteles con manga pastelera."
        ]
    }
}

# 2. Update 96#1
recipes["96#1"] = {
    "cluster": "96#1",
    "kind": "recipe",
    "source_refs": ["96#1", "267#1"],
    "source_hash": get_digest("96#1"),
    "recipe": {
        "title": "Quiche Lorraine clásico",
        "category": "Platos principales",
        "tags": ["horneado"],
        "servings": "6-8 porciones",
        "prep_time": "25 min",
        "cook_time": "30 min",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Masa",
                "items": [
                    "1 masa de pie sin hornear"
                ]
            },
            {
                "name": "Relleno",
                "items": [
                    "1/2 libra de tocino frito y picado",
                    "1/2 taza de cebolla finamente picada",
                    "1/2 libra de queso suizo o gruyere rallado",
                    "3 huevos grandes batidos",
                    "1 taza de crema agria",
                    "1/2 taza de leche con 1 cucharada de maicena disuelta",
                    "1/2 cucharadita de sal",
                    "Nuez moscada o pimienta de cayena al gusto"
                ]
            }
        ],
        "steps": [
            "Freír el tocino hasta dorar y escurrir; en la misma grasa sofreír la cebolla picada.",
            "En el fondo de la masa de pie colocar el tocino, cebolla y el queso suizo o gruyere rallado.",
            "Batir los huevos con la crema agria, la leche con maicena, sal y nuez moscada o pimienta de cayena.",
            "Verter la mezcla líquida sobre el queso y tocino.",
            "Hornear a 350°F por aproximadamente 30 minutos o hasta que cuaje y dore la superficie."
        ],
        "teacher_notes": [],
        "notes": [
            "Receta anotada también en apuntes de Edith's Kitchen."
        ]
    }
}

# 3. Update 115#1
recipes["115#1"] = {
    "cluster": "115#1",
    "kind": "recipe",
    "source_refs": ["115#1", "258#1"],
    "source_hash": get_digest("115#1"),
    "recipe": {
        "title": "Pie de pollo",
        "category": "Platos principales",
        "tags": ["horneado", "pollo"],
        "servings": "6-8 porciones",
        "prep_time": "25 min",
        "cook_time": "20 a 30 minutos",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Masa",
                "items": [
                    "1 receta de masa de pie doble"
                ]
            },
            {
                "name": "Relleno de pollo",
                "items": [
                    "3 pechugas de pollo cocidas y desmenuzadas",
                    "2 cucharadas de tomate picado",
                    "2 cucharadas de mantequilla",
                    "1 zanahoria cocida cortada en cuadritos",
                    "1 taza de arvejas cocidas",
                    "3 cucharadas de cebolla picada",
                    "1/2 taza de chile pimiento picado",
                    "2 huevos batidos",
                    "1 taza de crema",
                    "Sal y pimienta al gusto"
                ]
            }
        ],
        "steps": [
            "Freír en mantequilla la cebolla, tomate y chile pimiento.",
            "Agregar el pollo desmenuzado, la zanahoria y las arvejas. Sazonar con sal y pimienta.",
            "Añadir la crema y los huevos batidos, mezclando bien.",
            "Forrar un molde de pie con la mitad de la masa, rellenar con la mezcla de pollo y cubrir con el resto de la masa.",
            "Hornear a 350°F por 20 a 30 minutos hasta que la masa esté dorada."
        ],
        "teacher_notes": [],
        "notes": [
            "Edith's Kitchen."
        ]
    }
}

# 4. Update 153#1
recipes["153#1"] = {
    "cluster": "153#1",
    "kind": "recipe",
    "source_refs": ["153#1", "287#1"],
    "source_hash": get_digest("153#1"),
    "recipe": {
        "title": "Enchiladas suizas",
        "category": "Platos principales",
        "tags": ["pollo", "horneado"],
        "servings": "",
        "prep_time": "",
        "cook_time": "",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Salsa y relleno",
                "items": [
                    "6 a 8 miltomates",
                    "4 tomates verdes",
                    "1 cebolla",
                    "1 diente de ajo",
                    "2 cucharadas de crema agria",
                    "Queso Oaxaca o mozzarella",
                    "1 cucharada de cilantro picado",
                    "Tortillas de maíz y pollo (relleno)"
                ]
            }
        ],
        "steps": [
            "Cocer los miltomates y tomates verdes con cebolla y ajo.",
            "Licuar con la crema agria y el cilantro picado.",
            "Rellenar las tortillas con pollo, bañar con la salsa verde suiza y cubrir con queso Oaxaca o mozzarella.",
            "Gratinar en el horno hasta dorar el queso."
        ],
        "teacher_notes": [
            "Catedrática: AEH. Margarita de Sánchez (IFES)."
        ],
        "notes": [
            "Versión condensada en página 287 y extendida en página 153."
        ]
    }
}

# 5. Update 209#2
recipes["209#2"] = {
    "cluster": "209#2",
    "kind": "recipe",
    "source_refs": ["209#2", "276#1"],
    "source_hash": get_digest("209#2"),
    "recipe": {
        "title": "Turrón",
        "category": "Básicos y rellenos",
        "tags": ["sin horno"],
        "servings": "",
        "prep_time": "",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "Miel y merengue",
                "items": [
                    "1 taza de azúcar",
                    "1/4 taza de agua para punto de hebra (o 3/4 taza de agua)",
                    "1/2 onza de polvo de clara (merengue)"
                ]
            }
        ],
        "steps": [
            "Poner el azúcar con el agua al fuego para hacer una miel a punto de hebra o bola suave.",
            "Batir el polvo de clara a velocidad alta hasta que forme picos firmes.",
            "Disminuir la velocidad e incorporar la miel caliente en forma de hilo continuo batiendo hasta obtener brillo y firmeza."
        ],
        "teacher_notes": [
            "No mover el almíbar en exceso mientras hierve para que no se azucare."
        ],
        "notes": [
            "Técnicas Culinarias."
        ]
    }
}

# 6. 256#2
recipes["256#2"] = {
    "cluster": "256#2",
    "kind": "recipe",
    "source_refs": ["256#2"],
    "source_hash": get_digest("256#2"),
    "recipe": {
        "title": "Coco rallado de color",
        "category": "Básicos y rellenos",
        "tags": ["sin horno", "rápido", "vegetariano"],
        "servings": "",
        "prep_time": "5 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1/2 cucharadita de agua",
                    "Colorante vegetal líquido (unas gotas)",
                    "1 1/2 taza de coco rallado deshidratado"
                ]
            }
        ],
        "steps": [
            "En un tazón pequeño mezclar el agua con el colorante vegetal deseado (pocas gotas).",
            "Agregar el coco y mezclar bien con un tenedor hasta que tome un color parejo. Dejar secar sobre papel encerado."
        ],
        "teacher_notes": [],
        "notes": [
            "Ideal para decorar pasteles, queques y galletas con colores temáticos o festivos."
        ]
    }
}

# 7. 256#3
recipes["256#3"] = {
    "cluster": "256#3",
    "kind": "recipe",
    "source_refs": ["256#3"],
    "source_hash": get_digest("256#3"),
    "recipe": {
        "title": "Coco tostado",
        "category": "Básicos y rellenos",
        "tags": ["horneado", "rápido", "vegetariano"],
        "servings": "",
        "prep_time": "2 min",
        "cook_time": "7 a 12 minutos",
        "temperature": "175°C",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Coco rallado"
                ]
            }
        ],
        "steps": [
            "Extender el coco en latas de hornear galletas.",
            "Hornear a 175°C de 7 a 12 minutos o hasta que esté ligeramente dorado, moviendo ocasionalmente."
        ],
        "teacher_notes": [],
        "notes": [
            "Cuidar con frecuencia en el horno para evitar que se queme."
        ]
    }
}

# 8. 257#1
recipes["257#1"] = {
    "cluster": "257#1",
    "kind": "recipe",
    "source_refs": ["257#1"],
    "source_hash": get_digest("257#1"),
    "recipe": {
        "title": "Pastel de zanahoria",
        "category": "Postres y pasteles",
        "tags": ["horneado"],
        "servings": "10-12 porciones",
        "prep_time": "20 min",
        "cook_time": "30 a 40 minutos",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Masa de zanahoria",
                "items": [
                    "2 tazas de azúcar",
                    "1 taza de aceite",
                    "4 huevos",
                    "1 cucharadita de sal",
                    "2 cucharaditas de bicarbonato",
                    "1 cucharadita de canela en polvo",
                    "3 tazas de zanahoria rallada cruda",
                    "2 tazas de harina",
                    "1 taza de nueces picadas",
                    "1 cucharadita de polvo de hornear (Royal)"
                ]
            },
            {
                "name": "Forro de queso crema",
                "items": [
                    "8 onzas de queso crema",
                    "2 cucharaditas de vainilla blanca",
                    "2 tazas de azúcar glass",
                    "6 cucharadas de mantequilla"
                ]
            }
        ],
        "steps": [
            "Batir el azúcar con el aceite, agregar los huevos uno a uno batiendo bien.",
            "Cernir los ingredientes secos: harina, sal, bicarbonato, canela y Royal; incorporar a la mezcla anterior.",
            "Agregar la zanahoria rallada y las nueces picadas.",
            "Verter en molde engrasado y enharinado. Hornear a 350°F por 30 a 40 minutos.",
            "Para el forro: batir el queso crema con la mantequilla, vainilla blanca y azúcar glass hasta obtener una consistencia cremosa y suave. Decorar el pastel una vez frío."
        ],
        "teacher_notes": [],
        "notes": [
            "Edith's Kitchen."
        ]
    }
}

# 9. 259#1
recipes["259#1"] = {
    "cluster": "259#1",
    "kind": "recipe",
    "source_refs": ["259#1"],
    "source_hash": get_digest("259#1"),
    "recipe": {
        "title": "Tres leches",
        "category": "Postres y pasteles",
        "tags": ["horneado", "festivo"],
        "servings": "10-12 porciones",
        "prep_time": "25 min",
        "cook_time": "30 minutos",
        "temperature": "350°F (180°C)",
        "ingredient_groups": [
            {
                "name": "Masa",
                "items": [
                    "9 huevos (separadas claras y yemas)",
                    "2 tazas de azúcar",
                    "2 tazas de harina de trigo cernida",
                    "1/2 taza de leche líquida",
                    "1 cucharadita de polvo de hornear",
                    "1 cucharadita de vainilla"
                ]
            },
            {
                "name": "Baño de tres leches",
                "items": [
                    "1 lata de leche condensada (14 oz)",
                    "1 lata de leche evaporada (14 oz)",
                    "1 vaso de crema pura de vaca",
                    "1 cucharadita de vainilla",
                    "2 cucharadas de licor (ron o brandy)"
                ]
            }
        ],
        "steps": [
            "Batir las claras a punto de nieve e incorporar poco a poco el azúcar.",
            "Añadir las yemas una a una batiendo constantemente.",
            "Incorporar con espátula la harina con el polvo de hornear alternando con la leche y la vainilla con movimientos envolventes.",
            "Verter en molde engrasado y enharinado. Hornear a 350°F (180°C) durante 30 minutos.",
            "Mezclar los ingredientes del baño: leche condensada, leche evaporada, crema, vainilla y licor.",
            "Pinchar el pastel caliente o tibio con un tenedor y bañar con la mezcla de tres leches. Refrigerar."
        ],
        "teacher_notes": [],
        "notes": [
            "Chef Violeta Ortiz."
        ]
    }
}

# 10. 260#1
recipes["260#1"] = {
    "cluster": "260#1",
    "kind": "recipe",
    "source_refs": ["260#1"],
    "source_hash": get_digest("260#1"),
    "recipe": {
        "title": "Galletas a dos tonos",
        "category": "Postres y pasteles",
        "tags": ["horneado", "chocolate"],
        "servings": "24 galletas",
        "prep_time": "25 min",
        "cook_time": "8 a 10 minutos",
        "temperature": "400°F",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1/2 taza de mantequilla",
                    "1 taza de azúcar morena",
                    "1 huevo",
                    "1/2 cucharadita de vainilla",
                    "1 3/4 tazas de harina",
                    "1/2 cucharadita de bicarbonato",
                    "3/4 cucharadita de sal",
                    "1/2 onza de chocolate amargo derretido"
                ]
            }
        ],
        "steps": [
            "Cremar la mantequilla con el azúcar morena, agregar el huevo y la vainilla.",
            "Cernir la harina con el bicarbonato y la sal; agregar a la mezcla.",
            "Dividir la masa en dos partes. A una parte agregarle el chocolate amargo derretido.",
            "Extender ambas masas por separado formando rectángulos iguales, colocar una sobre la otra y enrollar en forma de cilindro.",
            "Refrigerar hasta que esté firme. Cortar en rodajas finas y colocar en latas engrasadas.",
            "Hornear a 400°F durante 8 a 10 minutos."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 11. 261#1
recipes["261#1"] = {
    "cluster": "261#1",
    "kind": "recipe",
    "source_refs": ["261#1"],
    "source_hash": get_digest("261#1"),
    "recipe": {
        "title": "Galletas de mantequilla y almendra",
        "category": "Postres y pasteles",
        "tags": ["horneado"],
        "servings": "20 galletas",
        "prep_time": "20 min",
        "cook_time": "20 minutos",
        "temperature": "180°C",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "4 onzas de mantequilla",
                    "2 onzas de azúcar glass",
                    "1 yema de huevo",
                    "6 onzas de harina",
                    "2 onzas de almendras picadas tostadas",
                    "1/4 cucharadita de polvo de hornear",
                    "1/2 cucharadita de bicarbonato",
                    "2 cucharadas de ajonjolí tostado para decorar"
                ]
            }
        ],
        "steps": [
            "Batir la mantequilla con el azúcar glass hasta estar cremosa. Agregar la yema.",
            "Incorporar la harina cernida con el polvo de hornear y bicarbonato.",
            "Agregar las almendras picadas y amasar ligeramente.",
            "Formar bolitas, aplanar y pasar por el ajonjolí tostado.",
            "Colocar en latas para hornear y hornear a 180°C por 20 minutos."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 12. 262#1
recipes["262#1"] = {
    "cluster": "262#1",
    "kind": "recipe",
    "source_refs": ["262#1"],
    "source_hash": get_digest("262#1"),
    "recipe": {
        "title": "Pastel de mantequilla",
        "category": "Postres y pasteles",
        "tags": ["horneado"],
        "servings": "10-12 porciones",
        "prep_time": "20 min",
        "cook_time": "50 a 60 minutos",
        "temperature": "175°C",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "3 tazas de harina",
                    "1 3/4 tazas de azúcar",
                    "5 onzas de mantequilla pura sin sal",
                    "2 huevos",
                    "1 pizca de sal",
                    "2 1/2 cucharaditas de polvo de hornear",
                    "1 1/4 taza de leche",
                    "1/2 taza de pasas (opcional)"
                ]
            }
        ],
        "steps": [
            "Batir la mantequilla con el azúcar hasta que esté bien cremosa y blanca.",
            "Agregar los huevos uno a uno sin dejar de batir.",
            "Cernir la harina con el polvo de hornear y la sal; agregar a la mezcla alternando con la leche.",
            "Envolver las pasas previamente enharinadas.",
            "Verter en molde engrasado y hornear a 175°C por 50 a 60 minutos."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 13. 263#1
recipes["263#1"] = {
    "cluster": "263#1",
    "kind": "recipe",
    "source_refs": ["263#1"],
    "source_hash": get_digest("263#1"),
    "recipe": {
        "title": "Crema de almendra",
        "category": "Básicos y rellenos",
        "tags": ["sin horno", "rápido", "vegetariano"],
        "servings": "4 porciones",
        "prep_time": "5 min",
        "cook_time": "3 minutos",
        "temperature": "Fuego medio",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1 yema de huevo",
                    "1/3 taza de azúcar",
                    "1 1/2 tazas de leche",
                    "2 cucharadas de maicena",
                    "1 cucharadita de esencia de almendra",
                    "1/4 taza de almendra fileteada tostada"
                ]
            }
        ],
        "steps": [
            "Disolver la maicena en un poco de leche fría.",
            "En una olla mezclar el resto de la leche con el azúcar y la yema batida.",
            "Agregar la maicena disuelta y cocinar a fuego medio moviendo constantemente durante 3 minutos o hasta que espese.",
            "Retirar del fuego, añadir la esencia de almendra y las almendras fileteadas. Dejar enfriar cubierta con plástico."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 14. 264#1
recipes["264#1"] = {
    "cluster": "264#1",
    "kind": "recipe",
    "source_refs": ["264#1"],
    "source_hash": get_digest("264#1"),
    "recipe": {
        "title": "Pretzelz de almendra",
        "category": "Postres y pasteles",
        "tags": ["horneado"],
        "servings": "20 piezas",
        "prep_time": "20 min",
        "cook_time": "15 minutos",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1 taza de mantequilla",
                    "1 taza de azúcar",
                    "3 yemas de huevo",
                    "1 taza de almendras molidas con cáscara",
                    "Ralladura de media naranja",
                    "2 a 3 tazas de harina"
                ]
            }
        ],
        "steps": [
            "Batir la mantequilla con el azúcar, agregar las yemas una a una.",
            "Incorporar la ralladura de naranja y las almendras molidas.",
            "Agregar la harina poco a poco hasta formar una masa suave pero manejable.",
            "Refrigerar la masa durante 2 horas.",
            "Tomar porciones de masa, formar tiras cilíndricas delgadas y dar forma de pretzeles.",
            "Colocar en latas de hornear y hornear a 350°F por 15 minutos."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 15. 265#1
recipes["265#1"] = {
    "cluster": "265#1",
    "kind": "recipe",
    "source_refs": ["265#1"],
    "source_hash": get_digest("265#1"),
    "recipe": {
        "title": "Regalos de azúcar",
        "category": "Postres y pasteles",
        "tags": ["horneado", "festivo"],
        "servings": "24 galletas",
        "prep_time": "30 min",
        "cook_time": "8 a 12 minutos",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Masa de galletas especiadas",
                "items": [
                    "2 tazas de harina",
                    "3/4 cucharadita de sal",
                    "1/2 cucharadita de polvo de hornear",
                    "1/2 cucharadita de jengibre molido",
                    "3/4 cucharadita de canela molida",
                    "1/2 cucharadita de pimienta dulce molida",
                    "1/4 cucharadita de nuez moscada",
                    "5 onzas de mantequilla",
                    "2/3 taza de azúcar morena",
                    "1/2 cucharadita de vainilla",
                    "1 huevo"
                ]
            },
            {
                "name": "Glaseado",
                "items": [
                    "3 tazas de azúcar glass",
                    "1/4 taza de agua tibia",
                    "Colorantes vegetales rojo y verde"
                ]
            }
        ],
        "steps": [
            "Cernir la harina con la sal, polvo de hornear y especias (jengibre, canela, pimienta, nuez moscada).",
            "Batir la mantequilla con el azúcar morena, agregar el huevo y la vainilla.",
            "Incorporar los ingredientes secos formando una masa compacta. Envolver en plástico y refrigerar 1 hora.",
            "Extender la masa a 1/2 cm de grosor y cortar en cuadrados simulando paquetitos o regalos.",
            "Hornear a 350°F por 8 a 12 minutos. Dejar enfriar.",
            "Preparar el glaseado mezclando azúcar glass con el agua, separar y pintar de colores para decorar como cintas y lazos de regalo."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 16. 266#1
recipes["266#1"] = {
    "cluster": "266#1",
    "kind": "recipe",
    "source_refs": ["266#1"],
    "source_hash": get_digest("266#1"),
    "recipe": {
        "title": "Masa de pie",
        "category": "Panes y masas",
        "tags": ["horneado", "vegetariano"],
        "servings": "2 tartas",
        "prep_time": "15 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "4 barras de margarina bien fría",
                    "2 tazas de harina",
                    "1/4 taza de queso parmesano rallado",
                    "Agua con hielo (cantidad necesaria)",
                    "Clara, yema o leche para brochear (dar brillo)"
                ]
            }
        ],
        "steps": [
            "Cortar la margarina fría en cubitos e incorporar a la harina y queso parmesano con estribo o tenedor hasta obtener textura arenosa.",
            "Agregar agua con hielo por cucharadas hasta unir la masa sin amasar en exceso.",
            "Extender en el molde para pie, rellenar y barnizar con clara, yema o leche para que dore y tenga brillo."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 17. 268#1
recipes["268#1"] = {
    "cluster": "268#1",
    "kind": "recipe",
    "source_refs": ["268#1"],
    "source_hash": get_digest("268#1"),
    "recipe": {
        "title": "Tacos al pastor",
        "category": "Platos principales",
        "tags": ["carne"],
        "servings": "6 porciones",
        "prep_time": "30 min",
        "cook_time": "20 min",
        "temperature": "Sartén / Plancha caliente",
        "ingredient_groups": [
            {
                "name": "Adobo y carne",
                "items": [
                    "1 cucharada de ajo picado",
                    "100 gramos de cebolla",
                    "2 chiles guajillos remojados y limpios",
                    "1 cucharada de azúcar",
                    "50 cc de jugo de limón",
                    "50 cc de jugo de naranja",
                    "100 cc de vinagre de manzana",
                    "1 cucharada de orégano",
                    "1 cucharada de achiote en polvo (opcional)",
                    "100 cc de jugo de piña",
                    "Sal y pimienta al gusto",
                    "Carne de cerdo cortada en bisteces delgados"
                ]
            }
        ],
        "steps": [
            "Licuar todos los ingredientes del adobo: ajo, cebolla, chiles guajillo, azúcar, jugos de limón, naranja y piña, vinagre, orégano, achiote, sal y pimienta.",
            "Marinar la carne de cerdo en el adobo durante al menos 2 a 4 horas o toda la noche.",
            "Cocinar la carne asada o en sartén bien caliente hasta que esté dorada, picar finamente y servir en tortillas con cebolla, cilantro y piña."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 18. 269#1
recipes["269#1"] = {
    "cluster": "269#1",
    "kind": "recipe",
    "source_refs": ["269#1"],
    "source_hash": get_digest("269#1"),
    "recipe": {
        "title": "Nachos o papas supreme",
        "category": "Entradas y bocadillos",
        "tags": ["carne", "rápido"],
        "servings": "4-6 porciones",
        "prep_time": "15 min",
        "cook_time": "10 min",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Totopos de maíz o papas fritas",
                    "Queso spread derretido",
                    "Carne molida sazonada cocida",
                    "Tomate picado en cubitos",
                    "Tallos de cebollín picados",
                    "Crema agria"
                ]
            }
        ],
        "steps": [
            "Colocar una base de totopos o papas fritas en una bandeja.",
            "Bañar con el queso spread derretido caliente.",
            "Distribuir encima la carne molida sazonada, el tomate en cubitos y los tallos de cebollín picados.",
            "Coronar con cucharadas de crema agria antes de servir."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 19. 269#2
recipes["269#2"] = {
    "cluster": "269#2",
    "kind": "recipe",
    "source_refs": ["269#2"],
    "source_hash": get_digest("269#2"),
    "recipe": {
        "title": "Caldo tlalpeño",
        "category": "Sopas y cremas",
        "tags": ["pollo"],
        "servings": "4 porciones",
        "prep_time": "15 min",
        "cook_time": "25 min",
        "temperature": "Hervor suave",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Pollo cocido y desmenuzado en su caldo",
                    "Arroz cocido con arvejas, cilantro y cebolla",
                    "Ajo picado",
                    "Cebolla cortada en gajos",
                    "Clavos de olor",
                    "Cilantro picado",
                    "Aguacate en cubitos",
                    "Cebollín picado"
                ]
            }
        ],
        "steps": [
            "Preparar el caldo de pollo sazonado con cebolla en gajos, ajo picado y clavos de olor.",
            "En cada plato hondo servir una porción de arroz cocido con arvejas y pollo desmenuzado.",
            "Bañar con el caldo de pollo bien caliente.",
            "Decorar encima con aguacate picado, cilantro fresco picado y cebollín."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 20. 270#1
recipes["270#1"] = {
    "cluster": "270#1",
    "kind": "recipe",
    "source_refs": ["270#1"],
    "source_hash": get_digest("270#1"),
    "recipe": {
        "title": "Frijol colorado",
        "category": "Platos principales",
        "tags": ["guiso", "vegetariano"],
        "servings": "6 porciones",
        "prep_time": "20 min",
        "cook_time": "1 hora",
        "temperature": "Fuego lento",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Frijol colorado",
                    "2 chiles pimientos",
                    "7 miltomates",
                    "4 tomates",
                    "3 dientes de ajo",
                    "2 cebollas",
                    "Pepita tostada y molida",
                    "Tomillo y laurel",
                    "Sal al gusto"
                ]
            }
        ],
        "steps": [
            "Poner a cocer los frijoles colorados con tomillo, laurel, ajo y cebolla.",
            "Asar o cocer los tomates, miltomates, chiles pimientos, cebolla y ajos; licuar finamente con la pepita tostada para formar el recado.",
            "Agregar el recado licuado a los frijoles cocidos y dejar hervir a fuego lento para que espese e integren los sabores."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 21. 270#2
recipes["270#2"] = {
    "cluster": "270#2",
    "kind": "recipe",
    "source_refs": ["270#2"],
    "source_hash": get_digest("270#2"),
    "recipe": {
        "title": "Chimichurri",
        "category": "Salsas y aderezos",
        "tags": ["sin horno", "vegetariano", "rápido"],
        "servings": "2 tazas",
        "prep_time": "15 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1 manojo de cilantro fresco picado",
                    "Hojas de albahaca verde picadas",
                    "Aceite de oliva o vegetal",
                    "4 cebollas grandes finamente picadas",
                    "3 cabezas de ajo peladas y picadas",
                    "Vinagre de manzana",
                    "Vino blanco o tinto",
                    "Sal y pimienta al gusto"
                ]
            }
        ],
        "steps": [
            "Picar finamente el cilantro, albahaca, ajos y cebollas.",
            "Mezclar en un tazón hondo o frasco con abundante aceite de oliva.",
            "Agregar vinagre de manzana y vino al gusto.",
            "Sazonar con sal y pimienta recién molida. Dejar reposar para que se concentren los aromas."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 22. 271#1
recipes["271#1"] = {
    "cluster": "271#1",
    "kind": "recipe",
    "source_refs": ["271#1"],
    "source_hash": get_digest("271#1"),
    "recipe": {
        "title": "Burrito",
        "category": "Platos principales",
        "tags": ["carne", "rápido"],
        "servings": "4 porciones",
        "prep_time": "10 min",
        "cook_time": "10 min",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Tortillas de harina grandes",
                    "Carne molida preparada con salsa",
                    "Arroz blanco cocido",
                    "Crema",
                    "Queso rallado"
                ]
            }
        ],
        "steps": [
            "Calentar las tortillas de harina hasta que estén suaves y flexibles.",
            "Colocar en el centro una capa de carne molida guisada con salsa y arroz blanco.",
            "Añadir crema y queso al gusto.",
            "Doblar los bordes laterales hacia adentro y enrollar firmemente formando el burrito."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 23. 272#1
recipes["272#1"] = {
    "cluster": "272#1",
    "kind": "recipe",
    "source_refs": ["272#1"],
    "source_hash": get_digest("272#1"),
    "recipe": {
        "title": "Salsa tártara",
        "category": "Salsas y aderezos",
        "tags": ["sin horno", "vegetariano", "rápido"],
        "servings": "1 taza",
        "prep_time": "10 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1 taza de mayonesa",
                    "Jugo de 1 limón",
                    "Pepinillos agridulces o salados picados finamente",
                    "1 huevo duro finamente picado",
                    "Alcaparras picadas",
                    "1 cucharadita de mostaza",
                    "Perejil fresco finamente picado"
                ]
            }
        ],
        "steps": [
            "En un tazón mezclar la mayonesa con el jugo de limón y la mostaza.",
            "Incorporar los pepinillos, las alcaparras y el perejil picado.",
            "Agregar el huevo duro picado con cuidado para no deshacerlo por completo. Refrigerar antes de servir."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 24. 272#2
recipes["272#2"] = {
    "cluster": "272#2",
    "kind": "recipe",
    "source_refs": ["272#2"],
    "source_hash": get_digest("272#2"),
    "recipe": {
        "title": "Hilachas",
        "category": "Platos principales",
        "tags": ["carne", "guiso"],
        "servings": "6 porciones",
        "prep_time": "25 min",
        "cook_time": "45 min",
        "temperature": "Fuego lento",
        "ingredient_groups": [
            {
                "name": "Carne y acompañamiento",
                "items": [
                    "Carne de res para hilachas (falda o bolovique)",
                    "Laurel y tomillo",
                    "Papas pequeñas con cáscara (partidas)"
                ]
            },
            {
                "name": "Salsa / Recado",
                "items": [
                    "6 tomates maduros",
                    "1 chile pimiento",
                    "8 miltomates",
                    "2 dientes de ajo",
                    "2 cebollas",
                    "Sal, pimienta y comino"
                ]
            }
        ],
        "steps": [
            "Cocinar la carne en olla de presión con agua, laurel, tomillo y sal hasta que esté muy suave; retirar y deshilachar la carne reservando el caldo.",
            "Asar o cocer los tomates, miltomates, chile pimiento, ajos y cebollas; licuar con un poco de caldo y sazonar con comino, sal y pimienta.",
            "En una olla colocar la salsa, añadir las papas pequeñas y cocinar hasta que estén tiernas.",
            "Incorporar la carne deshilachada y hervir todo junto a fuego suave hasta espesar."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 25. 273#1
recipes["273#1"] = {
    "cluster": "273#1",
    "kind": "recipe",
    "source_refs": ["273#1"],
    "source_hash": get_digest("273#1"),
    "recipe": {
        "title": "Lasagna",
        "category": "Platos principales",
        "tags": ["carne", "horneado"],
        "servings": "6-8 porciones",
        "prep_time": "30 min",
        "cook_time": "35 min",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Láminas de pasta para lasaña",
                    "Carne molida de res",
                    "Zanahoria picada finamente",
                    "Salsa de tomate",
                    "Nuez moscada",
                    "Sal y pimienta",
                    "Queso mozzarella rallado"
                ]
            }
        ],
        "steps": [
            "Preparar la carne molida sofriéndola con zanahoria, sazonar con sal, pimienta, nuez moscada y mezclar con la salsa de tomate.",
            "Cocer las láminas de pasta según las instrucciones del paquete.",
            "En un pyrex colocar capas alternadas de pasta, salsa con carne y queso mozzarella.",
            "Terminar con abundante queso y hornear hasta que esté bien gratinada."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 26. 274#1
recipes["274#1"] = {
    "cluster": "274#1",
    "kind": "recipe",
    "source_refs": ["274#1"],
    "source_hash": get_digest("274#1"),
    "recipe": {
        "title": "Pollo guisado con arroz",
        "category": "Platos principales",
        "tags": ["pollo", "guiso"],
        "servings": "4-6 porciones",
        "prep_time": "20 min",
        "cook_time": "40 min",
        "temperature": "Fuego medio",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Piezas de pollo",
                    "Chile pimiento",
                    "Miltomate",
                    "Tomate",
                    "Laurel y tomillo",
                    "Cebolla y ajo",
                    "Sal y pimienta"
                ]
            }
        ],
        "steps": [
            "Cocer o guisar las piezas de pollo con chile pimiento, miltomates, tomate, cebolla, ajo, laurel y tomillo.",
            "Cocinar a fuego lento hasta que el pollo esté tierno y la salsa espese.",
            "Acompañar y servir con arroz cocido."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 27. 274#2
recipes["274#2"] = {
    "cluster": "274#2",
    "kind": "recipe",
    "source_refs": ["274#2", "285#1"],
    "source_hash": get_digest("274#2"),
    "recipe": {
        "title": "Arroz cocido",
        "category": "Platos principales",
        "tags": ["vegetariano"],
        "servings": "4-6 porciones",
        "prep_time": "10 min",
        "cook_time": "20 min",
        "temperature": "Fuego lento",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Arroz corriente",
                    "Tomate",
                    "2 miltomates",
                    "Chile pimiento",
                    "Cebolla",
                    "Clavo",
                    "Pimienta",
                    "Zanahoria",
                    "Papa",
                    "Agua o caldo",
                    "Aceite o mantequilla",
                    "Sal al gusto"
                ]
            }
        ],
        "steps": [
            "Sofreír el arroz corriente con cebolla, tomate, miltomates y chile pimiento.",
            "Agregar agua o caldo, clavo, pimienta, zanahoria y papa cortadas en cubitos.",
            "Cocinar tapado a fuego bajo hasta que el grano esté suave y el líquido se haya consumido por completo."
        ],
        "teacher_notes": [],
        "notes": [
            "Anotado en dos versiones complementarias en las páginas 274 y 285."
        ]
    }
}

# 28. 275#1
recipes["275#1"] = {
    "cluster": "275#1",
    "kind": "recipe",
    "source_refs": ["275#1"],
    "source_hash": get_digest("275#1"),
    "recipe": {
        "title": "Crema pastelera",
        "category": "Básicos y rellenos",
        "tags": ["sin horno", "vegetariano"],
        "servings": "2 tazas",
        "prep_time": "10 min",
        "cook_time": "10 min",
        "temperature": "Fuego lento",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1/2 litro de leche",
                    "1 vaina de vainilla",
                    "125 gramos de azúcar",
                    "40 gramos de fécula de maíz",
                    "4 yemas de huevo"
                ]
            }
        ],
        "steps": [
            "Hervir la leche con la vaina de vainilla abierta; retirar del fuego y dejar infusionar.",
            "En un tazón batir las yemas de huevo con el azúcar hasta blanquear, luego incorporar la fécula de maíz.",
            "Colar la leche tibia sobre la mezcla de yemas batiendo constantemente.",
            "Regresar la preparación al fuego lento, batiendo continuamente con batidor de alambre hasta que espese y hierva 1 minuto.",
            "Retirar del fuego y dejar enfriar cubierta con papel film pegado a la superficie."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 29. 277#1
recipes["277#1"] = {
    "cluster": "277#1",
    "kind": "recipe",
    "source_refs": ["277#1"],
    "source_hash": get_digest("277#1"),
    "recipe": {
        "title": "Cupcakes",
        "category": "Postres y pasteles",
        "tags": ["horneado"],
        "servings": "24 cupcakes",
        "prep_time": "20 min",
        "cook_time": "20 min",
        "temperature": "350°F (180°C)",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "4 1/2 tazas de harina de fuerza",
                    "2 1/2 cucharadas de levadura",
                    "3/4 cucharada de sal",
                    "1 taza + 2 cucharadas soperas de mantequilla a temperatura ambiente",
                    "2 1/2 tazas de azúcar",
                    "6 huevos grandes",
                    "2 cucharadas de vainilla",
                    "1 1/4 taza de leche"
                ]
            }
        ],
        "steps": [
            "Cremar la mantequilla con el azúcar hasta que esponje.",
            "Añadir los huevos uno a uno, luego la vainilla.",
            "Cernir la harina con la levadura y la sal; agregar a la mezcla alternando con la leche.",
            "Repartir en moldes para cupcakes con capacillos y hornear a 350°F (180°C) hasta que al insertar un palillo salga limpio."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 30. 277#2
recipes["277#2"] = {
    "cluster": "277#2",
    "kind": "recipe",
    "source_refs": ["277#2"],
    "source_hash": get_digest("277#2"),
    "recipe": {
        "title": "Butter cream",
        "category": "Básicos y rellenos",
        "tags": ["sin horno", "vegetariano", "rápido"],
        "servings": "Para 24 cupcakes",
        "prep_time": "15 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "6 tazas de azúcar glass",
                    "1 taza de manteca vegetal",
                    "4 cucharadas de leche",
                    "2 cucharaditas de vainilla"
                ]
            }
        ],
        "steps": [
            "Acremar la manteca vegetal en batidora.",
            "Agregar gradualmente el azúcar glass alternando con la leche y la vainilla.",
            "Batir a velocidad media-alta hasta que quede suave y esponjoso para decorar."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 31. 278#1
recipes["278#1"] = {
    "cluster": "278#1",
    "kind": "recipe",
    "source_refs": ["278#1"],
    "source_hash": get_digest("278#1"),
    "recipe": {
        "title": "Quesadilla",
        "category": "Panes y masas",
        "tags": ["horneado"],
        "servings": "12 porciones",
        "prep_time": "25 min",
        "cook_time": "40 min",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Masa de quesadilla",
                "items": [
                    "1/2 libra de mantequilla",
                    "2 tazas de azúcar",
                    "8 huevos",
                    "1 taza de harina de trigo",
                    "3 tazas de harina de arroz",
                    "2 cucharaditas de polvo de hornear",
                    "8 onzas de crema de leche",
                    "4 onzas de queso seco rallado",
                    "1/2 taza de leche"
                ]
            },
            {
                "name": "Para decorar",
                "items": [
                    "1/2 taza de azúcar mezclada con 3 cucharadas de canela en polvo"
                ]
            }
        ],
        "steps": [
            "Batir la mantequilla y el azúcar hasta que esté cremosa.",
            "Añadir uno a uno los huevos.",
            "Agregar las harinas y el polvo de hornear alternando con la leche.",
            "Luego agregamos la crema y el queso seco rallado.",
            "Verter en moldes y espolvorear por encima con la mezcla de azúcar y canela.",
            "Hornear a 350°F hasta que dore."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 32. 279#1
recipes["279#1"] = {
    "cluster": "279#1",
    "kind": "recipe",
    "source_refs": ["279#1"],
    "source_hash": get_digest("279#1"),
    "recipe": {
        "title": "Cheesecake",
        "category": "Postres y pasteles",
        "tags": ["horneado", "baño maría"],
        "servings": "8 porciones",
        "prep_time": "15 min",
        "cook_time": "45 min",
        "temperature": "325°F",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1/2 libra (250 gramos) de queso crema",
                    "2 huevos",
                    "1 cucharadita de vainilla",
                    "1 taza de crema agria",
                    "1 taza de azúcar"
                ]
            }
        ],
        "steps": [
            "Acremar el queso crema con el azúcar hasta que esté completamente suave.",
            "Agregar los huevos uno a uno, la vainilla y la crema agria.",
            "Verter en molde y hornear a baño maría a 325°F hasta que cuaje."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 33. 279#2
recipes["279#2"] = {
    "cluster": "279#2",
    "kind": "recipe",
    "source_refs": ["279#2"],
    "source_hash": get_digest("279#2"),
    "recipe": {
        "title": "Salsa marinara",
        "category": "Salsas y aderezos",
        "tags": ["vegetariano", "rápido"],
        "servings": "2 tazas",
        "prep_time": "10 min",
        "cook_time": "20 min",
        "temperature": "Fuego bajo",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Tomate",
                    "Cebolla",
                    "Ajo",
                    "Hierbas",
                    "Aceite de oliva",
                    "Sal y pimienta"
                ]
            }
        ],
        "steps": [
            "Sofreír cebolla y ajo picados en aceite de oliva.",
            "Agregar tomates picados o triturados y hierbas aromáticas.",
            "Sazonar con sal y pimienta y dejar cocinar a fuego bajo hasta que espese."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 34. 280#1
recipes["280#1"] = {
    "cluster": "280#1",
    "kind": "recipe",
    "source_refs": ["280#1"],
    "source_hash": get_digest("280#1"),
    "recipe": {
        "title": "Papas horneadas",
        "category": "Platos principales",
        "tags": ["horneado", "vegetariano"],
        "servings": "4 porciones",
        "prep_time": "10 min",
        "cook_time": "40 min",
        "temperature": "350°",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Papas cortadas en gajos",
                    "Aceite de oliva",
                    "Queso parmesano",
                    "Sal al gusto",
                    "Especias italianas",
                    "Ajo en polvo",
                    "Pimentón español"
                ]
            }
        ],
        "steps": [
            "Reunir todos los ingredientes secos en un bol.",
            "Las papas bañarlas con el aceite de oliva, y luego pasarles o agregarles la mezcla seca.",
            "Colocar sobre papel aluminio en una bandeja para hornear.",
            "Hornear por 40 min. a 350°."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 35. 281#1
recipes["281#1"] = {
    "cluster": "281#1",
    "kind": "recipe",
    "source_refs": ["281#1"],
    "source_hash": get_digest("281#1"),
    "recipe": {
        "title": "Ensalada fresas",
        "category": "Entradas y bocadillos",
        "tags": ["sin horno", "frutas", "vegetariano", "rápido"],
        "servings": "4 porciones",
        "prep_time": "15 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "Base de ensalada",
                "items": [
                    "Lechuga colocha verde y morada",
                    "Fresas cortadas",
                    "Queso fresco",
                    "Nueces, pasas",
                    "Manzana"
                ]
            },
            {
                "name": "Aliño",
                "items": [
                    "Aceite de oliva",
                    "Pimienta blanca",
                    "Limón",
                    "Sal de hierbas",
                    "1 jugo de naranja (opcional)"
                ]
            }
        ],
        "steps": [
            "Mezclar las lechugas, fresas, queso fresco, nueces, pasas y manzana.",
            "Para el aliño: licuar el aceite de oliva, pimienta blanca, limón, sal de hierbas y jugo de naranja.",
            "Colocar el aliño sobre la ensalada."
        ],
        "teacher_notes": [],
        "notes": [
            "Categoría manuscrita: Cena."
        ]
    }
}

# 36. 282#1
recipes["282#1"] = {
    "cluster": "282#1",
    "kind": "recipe",
    "source_refs": ["282#1"],
    "source_hash": get_digest("282#1"),
    "recipe": {
        "title": "Batido verde",
        "category": "Bebidas",
        "tags": ["sin horno", "vegetariano", "frutas", "rápido"],
        "servings": "1 porción",
        "prep_time": "5 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "Espinaca",
                    "Perejil",
                    "Piña",
                    "1 naranja",
                    "1 limón",
                    "Miel",
                    "250 ml de agua"
                ]
            }
        ],
        "steps": [
            "Colocarlo todo en la licuadora y servirlo."
        ],
        "teacher_notes": [],
        "notes": [
            "Categoría manuscrita: Cena."
        ]
    }
}

# 37. 282#2
recipes["282#2"] = {
    "cluster": "282#2",
    "kind": "recipe",
    "source_refs": ["282#2"],
    "source_hash": get_digest("282#2"),
    "recipe": {
        "title": "Batido",
        "category": "Bebidas",
        "tags": ["sin horno", "vegetariano", "frutas", "rápido"],
        "servings": "1 porción",
        "prep_time": "5 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "1 zanahoria",
                    "1 pepino",
                    "1 apio",
                    "2 manzanas",
                    "1 limón",
                    "Jengibre molido",
                    "250 ml de agua"
                ]
            }
        ],
        "steps": [
            "Colocarlo todo en la licuadora y servirlo."
        ],
        "teacher_notes": [],
        "notes": [
            "Categoría manuscrita: Cena."
        ]
    }
}

# 38. 283#1
recipes["283#1"] = {
    "cluster": "283#1",
    "kind": "recipe",
    "source_refs": ["283#1"],
    "source_hash": get_digest("283#1"),
    "recipe": {
        "title": "Huevos con hierbas",
        "category": "Platos principales",
        "tags": ["desayuno", "rápido", "vegetariano"],
        "servings": "1-2 porciones",
        "prep_time": "10 min",
        "cook_time": "10 min",
        "temperature": "Sartén a fuego suave",
        "ingredient_groups": [
            {
                "name": "",
                "items": [
                    "2 huevos",
                    "Cebolla",
                    "1/2 chile pimiento rojo",
                    "1/2 chile pimiento verde",
                    "1 zucchini",
                    "Especias",
                    "Pimienta blanca",
                    "Perejil",
                    "Orégano",
                    "Albahaca",
                    "Sal de hierbas"
                ]
            }
        ],
        "steps": [
            "Saltear la cebolla, pimientos y zucchini con las hierbas y especias.",
            "Batir los huevos con sal de hierbas y pimienta, incorporar a las verduras y cocinar hasta que cuaje."
        ],
        "teacher_notes": [],
        "notes": [
            "Categoría manuscrita: Cena."
        ]
    }
}

# 39. 284#1
recipes["284#1"] = {
    "cluster": "284#1",
    "kind": "recipe",
    "source_refs": ["284#1"],
    "source_hash": get_digest("284#1"),
    "recipe": {
        "title": "Ensalada murciana",
        "category": "Entradas y bocadillos",
        "tags": ["sin horno", "rápido"],
        "servings": "4 porciones",
        "prep_time": "20 min",
        "cook_time": "",
        "temperature": "",
        "ingredient_groups": [
            {
                "name": "Ingredientes de la ensalada",
                "items": [
                    "2 papas pequeñas",
                    "3 tomates pequeños",
                    "1 cebolla",
                    "2 huevos duros",
                    "Olivas negras",
                    "1 lata de atún (opcional)"
                ]
            },
            {
                "name": "Aliño",
                "items": [
                    "Sal de hierbas",
                    "Aceite de oliva",
                    "Vinagre de manzana"
                ]
            }
        ],
        "steps": [
            "Cocer las papas y los huevos duros; cortar en cubos junto con los tomates y cebolla.",
            "Mezclar con las olivas negras y el atún si se desea.",
            "Bañar con el aliño de sal de hierbas, aceite de oliva y vinagre de manzana."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# 40. 286#1
recipes["286#1"] = {
    "cluster": "286#1",
    "kind": "recipe",
    "source_refs": ["286#1"],
    "source_hash": get_digest("286#1"),
    "recipe": {
        "title": "Pavo",
        "category": "Platos principales",
        "tags": ["festivo", "carne", "horneado"],
        "servings": "10-12 porciones",
        "prep_time": "45 min",
        "cook_time": "3 horas",
        "temperature": "350°F",
        "ingredient_groups": [
            {
                "name": "Salmuera y adobo previo",
                "items": [
                    "Pavo",
                    "Sal, mostaza y pimienta",
                    "2 tazas de vino blanco",
                    "2 tazas de Coca-Cola",
                    "2 tazas de cerveza"
                ]
            },
            {
                "name": "Salsa para el pavo",
                "items": [
                    "6 ajos",
                    "Tomillo",
                    "Laurel",
                    "Pimienta molida",
                    "Nuez moscada",
                    "Clavo",
                    "Jengibre",
                    "Chile guajillo",
                    "Cebolla y tomate",
                    "Sal",
                    "Ketchup",
                    "Piña, manzana, pasas"
                ]
            }
        ],
        "steps": [
            "Sal, mostaza y pimienta se dejan en salmuera con el pavo.",
            "Se le aplican 2 tazas de vino blanco, 2 tazas de Coca-Cola y 2 tazas de cerveza.",
            "Para la salsa: licuar ajos, tomillo, laurel, pimienta molida, nuez moscada, clavo, jengibre, chile guajillo, cebolla, tomate, sal y ketchup.",
            "Agregar a la salsa piña, manzana y pasas.",
            "Bañar el pavo con la salsa y hornear."
        ],
        "teacher_notes": [],
        "notes": []
    }
}

# Write recipes
for cid, rdata in recipes.items():
    c = clusters[cid]
    path = cache_file(c)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rdata, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Wrote {path}")

print(f"Batch 30 recipes written: {len(recipes)} recipes.")
