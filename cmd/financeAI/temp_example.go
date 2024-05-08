// This is an example program the AI gave me on how to build a random forest model
// Just putting this here to make go.mod and go.sum happy, will eventuall move
// the parts of all of this into their seperate pkg's and delete this file

package main

// import (
// 	"fmt"

// 	"github.com/sjwhitworth/golearn/base"
// 	"github.com/sjwhitworth/golearn/ensemble"
// 	"github.com/sjwhitworth/golearn/evaluation"
// )

// func main() {
// 	// Load data
// 	rawData, err := base.ParseCSVToInstances("your_data.csv", true)
// 	if err != nil {
// 		panic(err)
// 	}

// 	// Initialize a Random Forest classifier
// 	rf := ensemble.NewRandomForest(100, 3) // 100 trees, using 3 features in each split

// 	// Create a train-test split (80-20)
// 	trainData, testData := base.InstancesTrainTestSplit(rawData, 0.8)

// 	// Fit the Random Forest model
// 	err = rf.Fit(trainData)
// 	if err != nil {
// 		panic(err)
// 	}

// 	// Predictions
// 	predictions, err := rf.Predict(testData)
// 	if err != nil {
// 		panic(err)
// 	}

// 	// Evaluate the model
// 	confusionMat, err := evaluation.GetConfusionMatrix(testData, predictions)
// 	if err != nil {
// 		panic(err)
// 	}

// 	fmt.Println("Random Forest Model Accuracy:", evaluation.GetAccuracy(confusionMat))
// }
