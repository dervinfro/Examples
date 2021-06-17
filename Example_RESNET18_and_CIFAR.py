'''
this is my personal attempt to use resnet18 with the CIFAR10 image datasets
'''
import numpy as np
import matplotlib.pyplot as plt
import torch
import torchvision.transforms as transforms
import torch.optim as optim
import time
from torchvision import models, datasets
from torch import nn
from collections import OrderedDict

transform = transforms.Compose([transforms.ToTensor(),
								transforms.Normalize((0.485, 0.456, 0.406), 
													(0.229, 0.224, 0.225))])

train_data = datasets.CIFAR10('data', train=True, download=True, transform=transform)
test_data = datasets.CIFAR10('data', train=False, download=True, transform=transform)

# .Dataloader is a generator.  To pull data from it, it needs to be looped/iterated.
# torch.Size([20(batch_size), 3, 32, 32]
train_loader = torch.utils.data.DataLoader(train_data, batch_size=64, shuffle=True)
test_loader = torch.utils.data.DataLoader(test_data, batch_size=64)

model = models.resnet18(pretrained=True)

#freeze parameters so we don't back propagate through them.  We don't back propagate due to this script using a pre-trained model.  
for param in model.parameters():
	param.requires_grad = False
	
'''
The current resnet18 model has the following final fully-connected (fc) layer:
	(fc): Linear(in_features=512, out_features=1000, bias=True)
The out_features is set to 1000 because this model was pretrained on ImageNet.
The classifier will have to be changed to accept the following image classes:
	classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
	           'dog', 'frog', 'horse', 'ship', 'truck']
'''

classifier = nn.Sequential(OrderedDict([
				('fc1', nn.Linear(512, 256)),
				('relu', nn.ReLU()),
				('dropout', nn.Dropout(0.2)),
				('fc2', nn.Linear(256,10)),
				('output', nn.LogSoftmax(dim=1))
				]))
				
model.fc = classifier
#print(model)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

criterion = nn.NLLLoss() #negative log liklihood loss 

optimizer = optim.Adam(model.fc.parameters(), lr=0.001)

# specify the image classes
classes = ['airplane', 'automobile', 'bird', 'cat', 'deer',
           'dog', 'frog', 'horse', 'ship', 'truck']

#for x in range(2):
#	images, labels = next(iter(train_loader))
#	print("X: ", x, "Images: ", images, "\nLabels: ", labels[x], "\nClasses: ", classes[labels[x]])


model.to(device)

epochs = 1
steps = 0
running_loss = 0
print_every = 5
for epoch in range(epochs):
		for inputs, labels in train_loader:
				steps += 1
				
				trainloader_start_time = time.time()
				
				# Move input and label tensors to the default device
				inputs, labels = inputs.to(device), labels.to(device)
				
				optimizer.zero_grad()
				
				logps = model.forward(inputs)
				loss = criterion(logps, labels)
				loss.backward()
				optimizer.step()
				
				trainloader_end_time = time.time()
				print("Train time: {}".format(trainloader_end_time - trainloader_start_time))

				running_loss += loss.item()
				print("Running Loss: ", running_loss)
				
				if steps % print_every == 0:
						test_loss = 0
						accuracy = 0
						model.eval()
						with torch.no_grad():
								for inputs, labels in test_loader:
										testloader_start_time = time.time()
										
										inputs, labels = inputs.to(device), labels.to(device)
										logps = model.forward(inputs)
										batch_loss = criterion(logps, labels)
										
										testloader_end_time = time.time()
										print("Test time: {}".format(testloader_end_time - testloader_start_time))
										
										test_loss += batch_loss.item()
										print("Test Loss: ", test_loss)
										
										# Calculate accuracy
										ps = torch.exp(logps)
										top_p, top_class = ps.topk(1, dim=1)
										equals = top_class == labels.view(*top_class.shape)
										accuracy += torch.mean(equals.type(torch.FloatTensor)).item()
										
						print(f"Epoch {epoch+1}/{epochs}.. "
									f"Train loss: {running_loss/print_every:.3f}.. "
									f"Test loss: {test_loss/len(test_loader):.3f}.. "
									f"Test accuracy: {accuracy/len(test_loader):.3f}")
						running_loss = 0
						model.train()

'''
epochs = 10

for x in range(1, epochs+1):
	
	###############	
	##TRAIN MODEL##
	###############
	model.train()
	for images, labels in train_loader:
		
		train_loader_starttime = time.time()
		
		images, labels = images.to(device), labels.to(device)
		
		optimizer.zero_grad()	
		
		output = model(images)
		loss = criterion(output, labels)
		print("loss: ", loss)
		loss.backward()
		optimizer.step()
		
		
		train_loader_endtime = time.time()
		print("Train Time: {}".format(train_loader_endtime - train_loader_starttime))
		
		training_loss += loss.item()
		print("Train Loss: {}".format(training_loss))

	##############
	##TEST MODEL##
	##############
	model.eval()
	with torch.no_grad
		for image, label in test_loader:
			
			test_loader_starttime = time.time()
			
			image, label = image.to(device), label.to(device)
			output = model(image)
			loss = criterion(output, label)
			
			test_loader_endtime = time.time()
			print("Test time: {}".format(test_loader_endtime - test_loader_starttime))
			
			test_loss += output.item()
			print("Test Loss: {}".format(test_loss)
				
		


def imshow(img):
	img = img / 2 + 0.5 # unnormalize
	plt.imshow(np.transpose(img, (1, 2, 0)))  # convert from Tensor image

# plot the images in the batch, along with the corresponding labels
fig = plt.figure(figsize=(25, 4))
# display 20 images
for idx in range(20):
	ax = fig.add_subplot(2, 10, idx+1, xticks=[], yticks=[])
	imshow(images[idx])
	ax.set_title(classes[labels[idx]])
plt.show()


for ii, (image, label) in enumerate(train_loader):
	start = time.time()
	
	outputs = model.forward(image)
	loss = criterion(outputs, label)
	loss.backward()
	optimizer.step()
	
	end = time.time()
	
	print("Batch: {} - Time per batch: {:.3f}".format(ii, end - start))

	if ii == 5:
		break

'''