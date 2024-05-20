

```json
{
  "Objective": "Design a personalized and adaptable meal plan tailored to the client's specific details to support weight gain and six-pack abs. Prioritize nutritional accuracy, accommodate their vegetarian preferences, and offer a variety of recipes and ingredient substitutions to broaden meal choices.",
  
  "Client Details": {
    "numberOfDays": "$daysNumber",
    "mealsPerDay": "$mealsNumber",
    "fitnessGoals": "$fitnessGoals",
    "dietType": "$dietType",
    "dietRestrictions": "$dietRestrictions",
    "activityLevel": "$activityLevel",
    "medicalConditions": "$medicalConditions",
    "height": "$height",
    "heightType": "$heightType",
    "weight": "$weight",
    "weightType": "$weightType",
    "age": "$age",
    "gender": "$gender",
    "tastePreference": "$tastePreference",
    "description": "$description"
  },
  
  "Instructions": {
    "Calculate Daily Caloric Needs": {
      "Base Metabolic Rate": "Employ the Mifflin-St Jeor equation to determine BMR based on age, weight, height, and gender.",
      "Activity Adjustment": "Factor in the 'activityLevel' to establish maintenance calories.",
      "Target Calorie Intake": "Adjust calorie intake based on 'fitnessGoals' to determine the target daily calorie surplus or deficit."
    },

    "Set Flexible Macronutrient Targets": {
      "Initial Ratios": "Assign initial percentages of daily calories to proteins, fats, and carbohydrates, aligning with the 'dietType'.",
      "Meal-Specific Adjustments": "Suggest adjustments to macronutrient ratios across different meals within a day for optimal performance and physique goals (e.g., higher protein at breakfast, higher carbs around workouts)."
    },

    "Design and Verify Meals with Variations": {
      "Meal Creation": "Create meals adhering to the caloric and macronutrient targets. For each meal, provide a title, preparation time, a list of ingredients with precise measurements in grams, detailed cooking instructions, and nutritional profile including calories, carbohydrates, protein, and fats.",
      "Alternative Ingredients": "Provide alternative ingredient suggestions where applicable, emphasizing versatility and accommodating dietary restrictions."
    },

    "Verification": {
      "Nutritional Accuracy": "Cross-reference ingredient nutritional content with a reliable database to ensure each meal's total nutritional values align with the targets.",
      "Step-by-Step Verification": {
        "Step 1: Calculate each ingredient's contribution to the total nutritional values (calories, carbohydrates, protein, and fats).",
        "Step 2: Cross-verify these values with a reliable nutritional database.",
        "Step 3: Sum the nutritional values of all ingredients in a meal to get the total nutritional values.",
        "Step 4: Compare the total nutritional values against the target values to ensure accuracy."
      }
    }
  },
  
  "outputFormat": "Present the response in JSON format, matching the specifications without unrelated text or spaces. The output should be structured for direct incorporation into a JSON object, emphasizing accurate allocation of calories and macronutrients per meal, aligned with the individual's dietary needs and fitness goals."
}
```

### Key Additions:
- **Step-by-Step Verification**: Added within the **Verification** section to ensure calculations are accurate.
- **Natural Language Explanation**: Provides clarity on how to verify the nutritional values without needing programming languages.

____________


### Revised Prompt with Embedded Verification

```json
{
  "Objective": "Design a personalized and adaptable meal plan tailored to the client's specific details to support weight gain and six-pack abs. Prioritize nutritional accuracy, accommodate their vegetarian preferences, and offer a variety of recipes and ingredient substitutions to broaden meal choices.",
  
  "Client Details": {
    "numberOfDays": "$daysNumber",
    "mealsPerDay": "$mealsNumber",
    "fitnessGoals": "$fitnessGoals",
    "dietType": "$dietType",
    "dietRestrictions": "$dietRestrictions",
    "activityLevel": "$activityLevel",
    "medicalConditions": "$medicalConditions",
    "height": "$height",
    "heightType": "$heightType",
    "weight": "$weight",
    "weightType": "$weightType",
    "age": "$age",
    "gender": "$gender",
    "tastePreference": "$tastePreference",
    "description": "$description"
  },
  
  "Instructions": {
    "Calculate Daily Caloric Needs": {
      "Base Metabolic Rate": "Employ the Mifflin-St Jeor equation to determine BMR based on age, weight, height, and gender.",
      "Activity Adjustment": "Factor in the 'activityLevel' to establish maintenance calories.",
      "Target Calorie Intake": "Adjust calorie intake based on 'fitnessGoals' to determine the target daily calorie surplus or deficit."
    },

    "Set Flexible Macronutrient Targets": {
      "Initial Ratios": "Assign initial percentages of daily calories to proteins, fats, and carbohydrates, aligning with the 'dietType'.",
      "Meal-Specific Adjustments": "Suggest adjustments to macronutrient ratios across different meals within a day for optimal performance and physique goals (e.g., higher protein at breakfast, higher carbs around workouts)."
    },

    "Design and Verify Meals with Variations": {
      "Meal Creation": "Create meals adhering to the caloric and macronutrient targets. For each meal, provide a title, preparation time, a list of ingredients with precise measurements in grams, detailed cooking instructions, and nutritional profile including calories, carbohydrates, protein, and fats.",
      "Alternative Ingredients": "Provide alternative ingredient suggestions where applicable, emphasizing versatility and accommodating dietary restrictions."
    },

    "Verification": {
      "Nutritional Accuracy": "Follow these steps to ensure accuracy:",
      "Step 1": "For each ingredient, calculate its contribution to the total nutritional values (calories, carbohydrates, protein, and fats).",
      "Step 2": "Cross-verify these values with a reliable nutritional database.",
      "Step 3": "Sum the nutritional values of all ingredients in a meal to get the total nutritional values.",
      "Step 4": "Compare the total nutritional values against the target values to ensure accuracy."
    }
  },
  
  "outputFormat": "Present the response in JSON format, matching the specifications without unrelated text or spaces. The output should be structured for direct incorporation into a JSON object, emphasizing accurate allocation of calories and macronutrients per meal, aligned with the individual's dietary needs and fitness goals."
}
```

### Key Additions:
- **Natural Language Verification**: Clearly added within the **Verification** section to guide the model through a step-by-step verification process.
- **Instructions Embedded**: Kept within the existing structure to ensure the model performs the verification as part of its response generation process.

________


### Final Revised Prompt with Detailed Step-by-Step Calculations

```json
{
  "Objective": "Design a personalized and adaptable meal plan tailored to the client's specific details to support weight gain and six-pack abs. Prioritize nutritional accuracy, accommodate their vegetarian preferences, and offer a variety of recipes and ingredient substitutions to broaden meal choices.",
  
  "Client Details": {
    "numberOfDays": "$daysNumber",
    "mealsPerDay": "$mealsNumber",
    "fitnessGoals": "$fitnessGoals",
    "dietType": "$dietType",
    "dietRestrictions": "$dietRestrictions",
    "activityLevel": "$activityLevel",
    "medicalConditions": "$medicalConditions",
    "height": "$height",
    "heightType": "$heightType",
    "weight": "$weight",
    "weightType": "$weightType",
    "age": "$age",
    "gender": "$gender",
    "tastePreference": "$tastePreference",
    "description": "$description"
  },
  
  "Instructions": {
    "Calculate Daily Caloric Needs": {
      "Base Metabolic Rate": "Employ the Mifflin-St Jeor equation to determine BMR based on age, weight, height, and gender. Show each step of the calculation:",
      "Step 1": "Calculate BMR using the formula: For men: BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) + 5. For women: BMR = (10 * weight in kg) + (6.25 * height in cm) - (5 * age) - 161.",
      "Step 2": "Adjust BMR based on activity level: Sedentary (BMR * 1.2), Lightly active (BMR * 1.375), Moderately active (BMR * 1.55), Very active (BMR * 1.725), Super active (BMR * 1.9).",
      "Step 3": "Determine the target calorie intake based on fitness goals: If the goal is weight gain, add a surplus (e.g., 500 calories). If the goal is weight loss, create a deficit (e.g., 500 calories)."
    },

    "Set Flexible Macronutrient Targets": {
      "Initial Ratios": "Assign initial percentages of daily calories to proteins, fats, and carbohydrates, aligning with the 'dietType'. Show the calculation for each macronutrient:",
      "Step 1": "Calculate total daily calories from each macronutrient: Protein (e.g., 30% of total calories), Fats (e.g., 25% of total calories), Carbohydrates (e.g., 45% of total calories).",
      "Step 2": "Convert these calories into grams: Protein and Carbohydrates (1 gram = 4 calories), Fats (1 gram = 9 calories)."
    },

    "Design and Verify Meals with Variations": {
      "Meal Creation": "Create meals adhering to the caloric and macronutrient targets. For each meal, provide a title, preparation time, a list of ingredients with precise measurements in grams, detailed cooking instructions, and nutritional profile including calories, carbohydrates, protein, and fats.",
      "Alternative Ingredients": "Provide alternative ingredient suggestions where applicable, emphasizing versatility and accommodating dietary restrictions."
    },

    "Verification": {
      "Nutritional Accuracy": "Follow these steps to ensure accuracy:",
      "Step 1": "For each ingredient, calculate its contribution to the total nutritional values (calories, carbohydrates, protein, and fats).",
      "Step 2": "Cross-verify these values with a reliable nutritional database.",
      "Step 3": "Sum the nutritional values of all ingredients in a meal to get the total nutritional values.",
      "Step 4": "Compare the total nutritional values against the target values to ensure accuracy. Show each step of the calculation and comparison."
    }
  },
  
  "outputFormat": "Present the response in JSON format, matching the specifications without unrelated text or spaces. The output should be structured for direct incorporation into a JSON object, emphasizing accurate allocation of calories and macronutrients per meal, aligned with the individual's dietary needs and fitness goals."
}
```

### Key Additions:
- **Detailed Step-by-Step Calculations**: Embedded within the **Instructions** section to ensure the model performs and shows its work for each calculation.
- **Verification**: Ensures accuracy by having the model show each step of the calculation and comparison process.

-----------



### Revised Prompt for Google Gemini Pro

---

## OBJECTIVE

Design a personalized and adaptable meal plan tailored to the client's specific details to support weight gain and six-pack abs. Prioritize nutritional accuracy, accommodate their vegetarian preferences, and offer a variety of recipes and ingredient substitutions to broaden meal choices. This plan will be tailored for a client based on specific input details and preferences, which you will calculate and output in JSON.

## INSTRUCTIONS

1. **Calculate Daily Caloric Needs:**
    - Use the Mifflin-St Jeor equation to determine the basal metabolic rate (BMR):
      - For males: `BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age + 5`
      - For females: `BMR = 10 * weight (kg) + 6.25 * height (cm) - 5 * age - 161`
    - Adjust for activity level to find maintenance calories:
      - `Maintenance calories = BMR * activity level factor`
    - Create a caloric deficit or surplus based on the fitness goals to calculate the target daily caloric intake:
      - `Target daily caloric intake = Maintenance calories + caloric adjustment`
    
    *Verification Step:* Display each calculation step for BMR and maintenance calories. Confirm the values before proceeding to the next step.

2. **Set Macronutrient Targets:**
    - Allocate percentages of daily calories to proteins, fats, and carbohydrates according to the dietary preference:
      - Example: `protein_percentage = 30`, `fat_percentage = 25`, `carb_percentage = 45`
    - Convert these percentages to gram measurements using the caloric content per gram for each macronutrient:
      - `Protein grams = (Target daily caloric intake * protein_percentage / 100) / 4`
      - `Fat grams = (Target daily caloric intake * fat_percentage / 100) / 9`
      - `Carbohydrate grams = (Target daily caloric intake * carb_percentage / 100) / 4`

    *Verification Step:* Display each calculation step for converting percentages to gram measurements. Confirm the values before proceeding to the next step.

3. **Design and Verify Meals:**
    - Develop meal plans that adhere to the caloric and macronutrient targets.
    - For each meal, specify:
        - Title
        - Preparation Time
        - Ingredients: List with exact measurements in grams.
        - Detailed Cooking Instructions
        - Nutritional Profile (calories, carbs, proteins, fats)
        - Health Tips related to ingredients and their benefits
    
    *Verification Step:* Verify the nutritional content of each ingredient using a standard nutritional database. Calculate and confirm the total nutritional values for each meal, ensuring they align with the set targets. Provide a detailed nutritional breakdown for verification.

## EXAMPLE OUTPUT
Present the response in JSON format, precisely matching the provided specifications without including unrelated text or spaces. The output MUST be structured for direct incorporation into a JSON object, emphasizing accurate allocation of calories and macronutrients per meal, in line with the individual's dietary needs and fitness goals. It's crucial that the meal plan's caloric distribution accurately mirrors the specified number of meals, ensuring each meal contributes appropriately to the total daily calorie allotment.

```json
{
  "Title": "Spicy Black Bean Wrap",
  "Ingredients": [
    { "Black beans": "100g (cooked)" },
    { "Whole wheat tortilla": "100g" },
    { "Lettuce": "50g" },
    { "Diced tomatoes": "30g" },
    { "Low-fat cheese": "20g" },
    { "Jalapeños": "10g" }
  ],
  "PreparationTime": "10 minutes",
  "DetailedCookingInstructions": [
    "Heat a skillet over medium heat.",
    "Place the tortilla on the skillet and heat until it is warm and pliable.",
    "Remove the tortilla from the skillet and lay it flat on a clean surface.",
    "Spread the black beans evenly across the center of the tortilla.",
    "Layer the lettuce, diced tomatoes, and jalapeños on top of the beans.",
    "Sprinkle the low-fat cheese evenly over the vegetables.",
    "Carefully roll the tortilla tightly around the filling, ensuring that the ends are tucked in to hold the contents.",
    "Cut the wrap in half, if desired, and serve immediately while warm."
  ],
  "NutritionalVerification": {
    "Calories": "487 kcal",
    "Carbs": "76.1g",
    "Protein": "24.36g",
    "Fats": "9.84g"
  },
  "AdditionalTips": [
    "Enhance flavor with fresh lime juice and cilantro.",
    "Increase dietary fiber by including additional vegetables like spinach."
  ]
}
```

## CLIENT DETAILS

Below are the details of the client. Use these inputs to calculate both the **basal metabolic rate (BMR)** and the **macronutrient targets**.

```json
{
  "inputs": {
    "numberOfDays": "$daysNumber",
    "mealsPerDay": "$mealsNumber",
    "fitnessGoals": "$fitnessGoals",
    "dietType": "$dietType",
    "dietRestrictions": "$dietRestrictions",
    "activityLevel": "$activityLevel",
    "medicalConditions": "$medicalConditions",
    "height": "$height",
    "heightType": "$heightType",
    "weight": "$weight",
    "weightType": "$weightType",
    "age": "$age",
    "gender": "$gender",
    "tastePreference": "$tastePreference",
    "description": "$description"
  }
}
```

---

### Adjustments
- **Markdown Formatting**: Reformatted the instructions and sections using markdown for better readability.
- **Step-by-Step Calculations**: Included clear steps for calculating BMR, maintenance calories, and macronutrient targets, ensuring the model shows its work.
- **Verification Steps**: Detailed steps to verify calculations at each stage to ensure accuracy.
- **Output Format**: Maintained the JSON output format to match the requirements.