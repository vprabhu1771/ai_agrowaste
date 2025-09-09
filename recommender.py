def get_recommendations(waste_type):
    recommendations = {
        "banana_stem": ["Make fiber boards", "Create banana paper", "Animal feed"],
        "paddy_husk": ["Biogas", "Ash for bricks", "Organic fertilizer"],
        "sugarcane_bagasse": ["Biofuel", "Paper pulp", "Compost"]
    }
    return recommendations.get(waste_type, ["No suggestions available"])
