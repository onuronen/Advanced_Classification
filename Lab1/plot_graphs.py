import matplotlib.pyplot as plt

datasets = ["mnist_d", "mnist_f", "cifar_10", "cifar_100_f", "cifar_100_c"]
accuracies_ann = [97.49, 87.02, 36.22, 5.62, 28.1]
accuracies_cnn = [99.06, 92.66, 68.04, 34.91, 48.66]

x_pos = [i for i, _ in enumerate(datasets)]

"""
plt.bar(x_pos, accuracies_ann, color='green')
plt.xlabel("Datasets")
plt.ylabel("Accuracy(%)")
plt.title("ANN Accuracy Graph")
plt.xticks(x_pos, datasets)
plt.savefig("ANN_Accuracy_Plot.pdf")
plt.show()

"""


plt.bar(x_pos, accuracies_cnn, color='red')
plt.xlabel("Datasets")
plt.ylabel("Accuracy(%)")
plt.title("CNN Accuracy Graph")
plt.xticks(x_pos, datasets)
plt.savefig("CNN_Accuracy_Plot.pdf")
plt.show()

