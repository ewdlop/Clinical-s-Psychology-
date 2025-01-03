import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report, confusion_matrix

class PulleyPsychologyAnalyzer:
    def __init__(self):
        self.model = None
        self.label_encoders = {}
        self.feature_names = None
        self.class_names = None

    def generate_student_data(self, n_samples=500):
        """
        Generate synthetic student problem-solving data
        Includes cognitive, behavioral, and performance metrics
        """
        np.random.seed(42)
        
        # Cognitive factors
        spatial_ability = np.random.choice(['High', 'Medium', 'Low'], n_samples)
        physics_knowledge = np.random.choice(['Advanced', 'Intermediate', 'Basic'], n_samples)
        math_confidence = np.random.choice(['High', 'Medium', 'Low'], n_samples)
        
        # Problem-solving approach
        approach_type = np.random.choice([
            'Visual', 'Mathematical', 'Combined', 'Trial-and-Error'
        ], n_samples)
        
        # Behavioral indicators
        time_spent = np.random.normal(15, 5, n_samples)  # minutes
        attempts_made = np.random.poisson(3, n_samples)
        consulted_resources = np.random.choice(['Yes', 'No'], n_samples)
        
        # Performance metrics
        accuracy = np.random.uniform(0, 100, n_samples)
        
        # Create DataFrame
        data = pd.DataFrame({
            'spatial_ability': spatial_ability,
            'physics_knowledge': physics_knowledge,
            'math_confidence': math_confidence,
            'approach_type': approach_type,
            'time_spent': time_spent,
            'attempts_made': attempts_made,
            'consulted_resources': consulted_resources,
            'accuracy': accuracy
        })
        
        # Generate learning outcome based on factors
        data['learning_outcome'] = self.determine_learning_outcome(data)
        
        return data

    def determine_learning_outcome(self, data):
        """
        Determine learning outcome based on student characteristics
        Uses a rule-based approach to simulate real-world outcomes
        """
        outcomes = []
        
        for _, row in data.iterrows():
            score = 0
            
            # Weight different factors
            if row['spatial_ability'] == 'High':
                score += 2
            elif row['spatial_ability'] == 'Medium':
                score += 1
                
            if row['physics_knowledge'] == 'Advanced':
                score += 2
            elif row['physics_knowledge'] == 'Intermediate':
                score += 1
                
            if row['math_confidence'] == 'High':
                score += 2
            elif row['math_confidence'] == 'Medium':
                score += 1
                
            if row['approach_type'] == 'Combined':
                score += 2
            elif row['approach_type'] == 'Mathematical':
                score += 1
                
            if row['consulted_resources'] == 'Yes':
                score += 1
                
            if row['accuracy'] > 80:
                score += 2
            elif row['accuracy'] > 60:
                score += 1
                
            # Determine outcome based on score
            if score >= 8:
                outcomes.append('Mastery')
            elif score >= 5:
                outcomes.append('Proficient')
            else:
                outcomes.append('Developing')
                
        return outcomes

    def prepare_data(self, data):
        """Prepare data for the decision tree model"""
        # Encode categorical variables
        categorical_columns = [
            'spatial_ability', 'physics_knowledge', 'math_confidence',
            'approach_type', 'consulted_resources', 'learning_outcome'
        ]
        
        X = data.copy()
        for col in categorical_columns:
            self.label_encoders[col] = LabelEncoder()
            X[col] = self.label_encoders[col].fit_transform(X[col])
            
        # Store feature names and class names
        self.feature_names = list(X.columns[:-1])  # all except learning_outcome
        self.class_names = self.label_encoders['learning_outcome'].classes_
        
        # Split features and target
        y = X['learning_outcome']
        X = X.drop('learning_outcome', axis=1)
        
        return X, y

    def build_model(self, X, y):
        """Build and train the decision tree model"""
        self.model = DecisionTreeClassifier(
            max_depth=5,
            min_samples_split=20,
            min_samples_leaf=10,
            random_state=42,
            class_weight='balanced'
        )
        
        self.model.fit(X, y)

    def analyze_patterns(self, X, y):
        """Analyze learning patterns and success factors"""
        predictions = self.model.predict(X)
        feature_importance = pd.DataFrame({
            'feature': self.feature_names,
            'importance': self.model.feature_importances_
        }).sort_values('importance', ascending=False)
        
        return {
            'classification_report': classification_report(y, predictions),
            'feature_importance': feature_importance,
            'cv_scores': cross_val_score(self.model, X, y, cv=5)
        }

    def plot_decision_tree(self):
        """Visualize the decision tree"""
        plt.figure(figsize=(20, 10))
        plot_tree(self.model, 
                 feature_names=self.feature_names,
                 class_names=self.class_names,
                 filled=True,
                 rounded=True)
        plt.title('Student Learning Pattern Decision Tree')
        plt.show()

    def plot_feature_importance(self, feature_importance):
        """Plot feature importance"""
        plt.figure(figsize=(10, 6))
        sns.barplot(x='importance', y='feature', data=feature_importance)
        plt.title('Factors Influencing Learning Outcomes')
        plt.xlabel('Importance Score')
        plt.show()

    def analyze_learning_paths(self, data):
        """Analyze common learning paths to success"""
        successful = data[data['learning_outcome'] == 'Mastery']
        
        paths = pd.DataFrame({
            'Approach': successful['approach_type'].value_counts(normalize=True),
            'Knowledge Level': successful['physics_knowledge'].value_counts(normalize=True),
            'Resource Use': successful['consulted_resources'].value_counts(normalize=True)
        })
        
        return paths

def main():
    # Create analyzer instance
    analyzer = PulleyPsychologyAnalyzer()
    
    # Generate synthetic student data
    print("Generating student data...")
    data = analyzer.generate_student_data()
    
    # Prepare data
    X, y = analyzer.prepare_data(data)
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    # Build and train model
    print("\nTraining model...")
    analyzer.build_model(X_train, y_train)
    
    # Analyze patterns
    print("\nAnalyzing learning patterns...")
    analysis = analyzer.analyze_patterns(X_test, y_test)
    
    print("\nClassification Report:")
    print(analysis['classification_report'])
    
    print("\nCross-validation scores:", 
          f"Mean: {analysis['cv_scores'].mean():.2f}, ",
          f"Std: {analysis['cv_scores'].std():.2f}")
    
    # Plot results
    analyzer.plot_decision_tree()
    analyzer.plot_feature_importance(analysis['feature_importance'])
    
    # Analyze successful learning paths
    paths = analyzer.analyze_learning_paths(data)
    print("\nSuccessful Learning Paths:")
    print(paths)

if __name__ == "__main__":
    main()
