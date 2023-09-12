class TumorModel:
    def __init__(self, initial_radius, genetics, signaling, angiogenesis, immune_response, hormones,
                 microenvironment, nutrition, oxygen, treatment_effectiveness,
                 microbiome, age_lifestyle, inflammation):
        # parameters
        self.initial_radius = initial_radius
        self.genetics = genetics
        self.signaling = signaling
        self.angiogenesis = angiogenesis
        self.immune_response = immune_response
        self.hormones = hormones
        self.microenvironment = microenvironment
        self.nutrition = nutrition
        self.oxygen = oxygen
        self.treatment_effectiveness = treatment_effectiveness
        self.microbiome = microbiome
        self.age_lifestyle = age_lifestyle
        self.inflammation = inflammation

        # defined weights for each parameter
        self.genetics_weight = 0.1
        self.signaling_weight = 0.2
        self.angiogenesis_weight = 0.05
        self.immune_response_weight = 0.1
        self.hormones_weight = 0.05
        self.microenvironment_weight = 0.1
        self.nutrition_weight = 0.05
        self.oxygen_weight = 0.05
        self.treatment_effectiveness_weight = 0.05
        self.microbiome_weight = 0.05
        self.age_lifestyle_weight = 0.05
        self.inflammation_weight = 0.05

        # calculate the tumor growth rate
        self.growth_rate = self.calculate_tumor_growth_rate()

    def calculate_tumor_growth_rate(self):
        growth_rate = (
            self.genetics * self.genetics_weight +
            self.signaling * self.signaling_weight +
            self.angiogenesis * self.angiogenesis_weight +
            self.immune_response * self.immune_response_weight +
            self.hormones * self.hormones_weight +
            self.microenvironment * self.microenvironment_weight +
            self.nutrition * self.nutrition_weight +
            self.oxygen * self.oxygen_weight +
            self.treatment_effectiveness * self.treatment_effectiveness_weight +
            self.microbiome * self.microbiome_weight +
            self.age_lifestyle * self.age_lifestyle_weight +
            self.inflammation * self.inflammation_weight
        )
        return growth_rate
