# The Most Important Algorithm in Machine Learning

![rw-book-cover](https://i.ytimg.com/vi/SmZmBKc7Lrs/maxresdefault.jpg)

## Metadata
- Author: [[Artem Kirsanov]]
- Date: 2024-03-31
- Full Title: The Most Important Algorithm in Machine Learning
- Category: #articles
- Summary: The text explains the significance of derivatives in minimizing the loss function in machine learning models through gradient descent. Derivatives help in determining the optimal direction to update model parameters for reducing loss. The chain rule is used to compute derivatives of complex functions by breaking them down into simpler components.
- URL: https://youtube.com/watch?v=SmZmBKc7Lrs&si=C1hkIsgWBgLqawbv

## Highlights
- hard to say who invented back propagation in the first place as certain Concepts can be traced back to Li needs in 17th century however it is believed that the first modern formulation of the algorithm still in use today was published by sepo linar in his master's thesis in 1970 although he did not reference any neural networks explicitly ([View Highlight](https://read.readwise.io/read/01htcgen4wvhwvjethn878tbfc))
- significant Milestone occurred in 1986 when David rumelhart Joffrey Hinton and Ronald Williams
  published a paper titled learning representations by back propagating errors ([View Highlight](https://read.readwise.io/read/01htcgeytrzfmry9yedj1yy7xy))
- back propagation algorithm to multi-layer perceptrons a type of a neural network and demonstrated for the first time that training with back propagation enables the network to successfully solve problems and develop meaningful representations at the hidden neuron level capturing important regularities in the task ([View Highlight](https://read.readwise.io/read/01htcgfm0k2xprxt4kyakznsvq))
- suppose you have collected a set of points XY on the plane and you want to describe their relationship ship to achieve this you
  need to fit a curve y of X that best represents the data since there are infinitely many possible functions we need to make some assumptions ([View Highlight](https://read.readwise.io/read/01htcgh7rf4tj38b6px9y3y0ey))
- the equation for the curve is as follows where each K is some arbitrary real number our job then becomes finding the configuration of k0 through K5 which leads to the best fitting curve ([View Highlight](https://read.readwise.io/read/01htcgj752548srh8s4mfrez43))
- we need an objective measurement a numerical value that quantifies the quality of a fit one popular method is to measure the square distance between data points and the fitted curve a high value suggests that the data points are significantly far
  from the curve indicating a poor approximation conversely low values indicate a better fit as the curve closely aligns with the data points ([View Highlight](https://read.readwise.io/read/01htcgkn5edjrnj3596e4nzkj2))
- commonly referred to as a loss and the objective is to minimize it ([View Highlight](https://read.readwise.io/read/01htcgkxgv398wsgn1tept36rp))
- function of parameters so people usually refer to it as a loss function ([View Highlight](https://read.readwise.io/read/01htcgmr2req2zvaxae0bddqj8))
- loss function which instead has six inputs numbers k0 through K5 and for each configuration it constructs the corresponding curve y calculates the distance between observed data points and the curve and outputs a single number the particular value of the loss ([View Highlight](https://read.readwise.io/read/01htcgp01avdsfbsr322jqmaw6))
- our job then becomes finding the
  configuration of case that yields a minimum loss or minimizing the loss function with respect to the coefficients then plugging these optimal cases into the general equation for the Curve will give us the best curve described in the data ([View Highlight](https://read.readwise.io/read/01htcgprzdb69hpcjdzs3g38w4))
- random perturbation method since we are essentially wandering in the dark not knowing in advance how each adjustment will affect the loss function this would certainly work but it's not very
  efficient ([View Highlight](https://read.readwise.io/read/01htcgtwkcrt1px379s2n39eeg))
- under the hood of our curve fitter have a special property to them something called differentiability that allows us to compute the optimal knob setting much more efficiently ([View Highlight](https://read.readwise.io/read/01htcgw105pfabwq58bf17wjmx))
- we are essentially asking the machine to predict the future and estimate the effect of the knob adjustment on the loss function without actually performing that adjustment calculating the loss and then reverting the knob back like we did previously wouldn't this glance into the future violate some sort of principle after all we are jumping to the result of the computation without performing it ([View Highlight](https://read.readwise.io/read/01htcgyw9mhzejxpj61ctd7a2q))
- we freeze five out of six knobs for example suppose someone tells you that the rest of them are already in the optimal position so all you need to do is to find the best value for one remaining kn
  essentially the machine now has only one variable parameter K1 that we can tweak and so the loss function is also a simpler function which accepts one number the knob setting and outputs another number the loss value as a function of one variable it can be conveniently visualized as a graph in a two-dimensional plane which captures the relationship between the input and the output ([View Highlight](https://read.readwise.io/read/01htch0jwcggqb5fh9gvr18qsx))
- we are essentially blind to how the function behaves in between the known points before we sample them ([View Highlight](https://read.readwise.io/read/01htch1nv7gnrywe7gcv80d6yc))
- we
  would like to know something more about the function not just each value at each point for example whether at this point the function is going up or down this information will ultimately guide our adjustments because if you know that the function is going down as you increase the input turning the knob to the right is a safe bad since you are guaranteed to decrease the loss with this manipulation ([View Highlight](https://read.readwise.io/read/01htch2j0g6fz6dceznwhha8f6))
- it makes sense to take the ratio Delta y over Delta X the amount of change in the output per unit change in the input ([View Highlight](https://read.readwise.io/read/01htch434c1menc6k865w24wkx))
- graphically this ratio corresponds to a slope of a straight line going through the points X not y KN and X Plus Delta X Y KN plus Delta y note notice that as we take
  smaller and smaller steps this straight line will more and more accurately align with the graph in the neighborhood of the point ([View Highlight](https://read.readwise.io/read/01htch4ryw47za4m555tzkp98n))
- limit of this ratio as Delta X goes to infinitely small values then this limiting case value which this ratio converges to for infinitesimally small Delta X's is what is called the derivative of a function and it is denoted by dy/ DX ([View Highlight](https://read.readwise.io/read/01htchbtdbd1hhfdfyrwnf49rx))
- at some point is the slope of the line that is tangent to the graph and thus corresponds to the instantaneous rate of change or steepness of that function around that point ([View Highlight](https://read.readwise.io/read/01htchc7yn60752wynh4n2myt4))
- this definition assigns to every function its derivative Alter Ego another function operating on the same input domain which carries information about the steepness of the original function ([View Highlight](https://read.readwise.io/read/01htch6z1kjh7dfem9fnmkkjs7))
- underlying loss as a function of K1 which is hidden from us we can also reason about its derivative another function of K1 which we also don't know that is equal to the steepness of the loss function at that point ([View Highlight](https://read.readwise.io/read/01htchf3z7xhc0893gdr5yw8ef))
- there is a mechanism for us to sample
  the derivative function as well so for every input value of K1 the machine will output the value of the loss and the local steepness of the loss function around that point ([View Highlight](https://read.readwise.io/read/01htchfwz3jtgdb2c0zc5gnn7g))
- start at some random position ask the machine for a value of the loss and the derivative of the loss function at that position take a tiny step in the direction opposite of the derivative if the derivative is negative it means that the function is going down and so if we want to arrive at the minimum we need to move in the direction of increase in value of K1 repeat this procedure until
  you reach the point where the derivative is zero ([View Highlight](https://read.readwise.io/read/01htchhpndhb6z3j0zthj0t9r2))
- essentially corresponds to the minimum where the tangent line is flat essentially each adjustment in such a guided fashion Works kind of like a ball rolling down the hill along the graph until it reaches a valley ([View Highlight](https://read.readwise.io/read/01htchhvvga0fr7e77nyajnk3t))
- by definition the derivative at each point tells us how the output changes per unit change of the input but now we have two different inputs should
  we nudge only K1 K2 or both essentially our function will have two different derivatives that are usually called partial derivatives ([View Highlight](https://read.readwise.io/read/01htchkh1amaj94zk5jekpag8b))
- two knobs the derivative of the loss function with respect to parameter K1 is written like this it is how much the output changes per unit change in K1 if you hold K2
  constant and conversely this expression tells you the rate of change of the output if you hold K1 constant and slightly Notch K2 geometrically you can imagine slicing the surface with planes parallel to the axis intersecting at the point of Interest K1 K2 so that each of the two cross-sections is like a one-dimensional graph of the loss ([View Highlight](https://read.readwise.io/read/01htchmymtbb6s0cwtf9rv2b55))
- people usually plug the two different values into a vector called a gradient Vector
  essentially this is a mapping from two input values to another two numbers where the first signifies how much the output changes per tiny change in the first input and similarly for the second input ([View Highlight](https://read.readwise.io/read/01htchq1gmzxb1g1wqvfhnqxk2))
- geometrically this Vector points in the direction of steepest Ascent so if you want to minimize a function like in the case for our loss we need to take steps in the direction opposite to this
  gradient this iterative procedure of nudging the parameters in the direction opposite of the gradient Vector is called gradient descent ([View Highlight](https://read.readwise.io/read/01htchqpmjyyzm5vfevbfx9f65))
- analogous to a ball rolling down the hill for the two-dimensional case ([View Highlight](https://read.readwise.io/read/01htchrr43pgn1e2z36r2b7x4d))
- partial derivatives essentially tell you which direction is downhill ([View Highlight](https://read.readwise.io/read/01htchs9728j69wx09hhm4e973))
- Beyond two Dimensions is impossible to visualize directly but the math stays exactly the
  same for instance if we are now free to tweak all the six knobs the loss function is a hypersurface in Six Dimensions and the gradient Vector now has six numbers packed into it but it still points in the direction of steepest ([View Highlight](https://read.readwise.io/read/01htchsw36xzv5g5txfg14gjd3))
- once we have a way of accessing the derivative we can perform gradient descent and efficiently find the minimum of the loss function thus solving the
  optimization problem ([View Highlight](https://read.readwise.io/read/01htchw0v766pmqk89yzcr6tqa))
- we have implicitly assumed the derivative information is given to us or that we can sample the derivative at a given point similarly to how we sample the loss function Itself by running the calculation of the machine but how do you actually find the derivative ([View Highlight](https://read.readwise.io/read/01htchwnvfce8g9rmyy4a8pmjj))
- the way we find
  derivatives of arbitrarily complex functions ([View Highlight](https://read.readwise.io/read/01htchxbwdeve1htgydp3pz9rr))
- in order to compute arbitrary
  derivatives we need a way to combine such Atomic building blocks together ([View Highlight](https://read.readwise.io/read/01htchyy9pcegyqcqfw4tw0gbb))
- The Chain rule which Powers the entire field of machine learning it tells you how to compute the derivative of a combination of two functions when one of them is an input to another ([View Highlight](https://read.readwise.io/read/01htcj2v7jd2nxbqgk5dwq8ks3))
- suppose you take one of those simpler machines which receives a single input x that you can vary with a knob and spits out an output
  J of X now you take a second machine of this kind which performs a different function f ofx what would happen if you connect them in sequence so that the output of the first machine is fed into the second one ([View Highlight](https://read.readwise.io/read/01htcj3daxfk33mkdssxkfcpa2))
- such a construction can be thought of as a single function which also receives one input number and
  gives an output by Computing a more complicated function which is a composition of the two simpler functions in fact if you put a black box around it to conceal the fact that there are actually two machines operating sequentially you can treat it as a single machine ([View Highlight](https://read.readwise.io/read/01htcj3wtxbw40hqj4jggqjt0w))
- suppose we know the individual derivatives of the two machines F and J if the knob is set at some value X local steepness of the first function is evaluated at X however the number that is fed into the second machine is not X because it was already processed by the first function so the thing that is being plugged into the second function is J of X and so the local rate of
  change of the second machine is thus the derivative of f evaluated at the point J of X ([View Highlight](https://read.readwise.io/read/01htcj5f88eapddmfg3fxran8v))
- imagine you nudge the knob X by a tiny amount Delta that input nudge when it comes out of the first machine will be multiplied by the derivative of J since the derivative is the rate of change in the output per unit change of the input ([View Highlight](https://read.readwise.io/read/01htcj611az2rmnb2a2kbmtkws))
- the output will increase by Delta multiplied by the derivative of J this expression is essentially a tiny nudge in the input to the second machine whose derivative at that point is given by this expression this means that for each Delta increase in the input we bump the output by this much ([View Highlight](https://read.readwise.io/read/01htcj6z5wyha5qgqqtymmddxg))
- you can think about it as a set of three interconnected Cog Wheels where the first one represents the input knob X and the other two wheels are functions J of X and F of J of X respectively when you Nodge the first wheel it induces a nudge in the middle wheel and the amplitude of that change is given by the derivative of J which in turn causes the Third Wheel to rotate and the amplitude of that resulting nudge is given by
  changing the derivatives together ([View Highlight](https://read.readwise.io/read/01htcj821gc06zxvqq97aenb1a))
- for each of our parameter knobs we will write down its effect on the loss in terms of simple easily differentiable operations ([View Highlight](https://read.readwise.io/read/01htcj96fzfj2gz93bckejzkcf))
- once we have that sequence of building blocks no matter how long we should be able to sequentially apply the chain rule to each of them in order to find the value of the derivative of the loss function with respect to each of the input knobs
  and perform iterative gradient descent to minimize the loss ([View Highlight](https://read.readwise.io/read/01htcj9sdrzh065ymhfr457fka))
- during optimization the data points are set in Stone so changing them in order
  to obtain a lower loss would make no sense ([View Highlight](https://read.readwise.io/read/01htcjaz0242cabrjpcq87mdm0))
- once we have all the existing numbers being fed into the machine we can start to break down the loss calculation ([View Highlight](https://read.readwise.io/read/01htcjbbtzr3qafy32kg4gef13))
- sum of weight and powers of X1 is the value of y predicted by the
  current curve F of X1 let's call it y1 hat ([View Highlight](https://read.readwise.io/read/01htcjd29cb59bdntx076sbvyn))
- we need to take the squared difference between the actual value and the predicted value this is how much the first data point contributes to the resulting value of the loss function repeating the same procedure ([View Highlight](https://read.readwise.io/read/01htcjdjj7h1mmhtpnbkvvj9yc))
- summing up the resulting squared distances gives us the overall total loss that we
  are trying to minimize ([View Highlight](https://read.readwise.io/read/01htcjdye3q5mamsj1fy8tkebz))
- finding the value of the loss for a given configuration of parameter and data knobs is known as the forward step ([View Highlight](https://read.readwise.io/read/01htcjefedsaxs1ny8gh0r3c6c))
- computational graph where each node is some simple operation like addition or
  multiplication forward step then corresponds to computations flowing from left to right ([View Highlight](https://read.readwise.io/read/01htcjexcvh61kena6zknqn766))
- to perform optimization we also need information about gradients how each knob influences the loss ([View Highlight](https://read.readwise.io/read/01htcjfcak5eqec2gsa0ksc1vq))
- the backward step and unroll the sequence of calculations in reverse order to find derivatives ([View Highlight](https://read.readwise.io/read/01htcjfk3ydqf8qcnqk5r0apd2))
- every
  note in our compute graph is an easily differentiable operation think of individual nodes as these tiny machines which simply add multiply or take Powers we know their derivatives and because their outputs are connected sequentially we can apply the chain rule ([View Highlight](https://read.readwise.io/read/01htcjga6d24qhc72tyz2fe851))
- for each node we can find its gradient the partial derivative of of the output loss with respect to that
  node ([View Highlight](https://read.readwise.io/read/01htcjgjrzjek7040qdx0ecpzp))
- consider a region of the compute graph where two number nodes A and B are being fed into a machine that performs addition and its result a plus b is further processed by the system to compute the overall output L suppose we already computed the gradient of a plus b earlier so that we know how nding this
  sum will affect the output ([View Highlight](https://read.readwise.io/read/01htcjhhv5vvs91543hsnv5nzw))
- consider a region of the compute graph where two number nodes A and B are being fed into a machine that performs addition and its result a plus b is further processed by the system to compute the overall output L ([View Highlight](https://read.readwise.io/read/01htcjjca85drxg5bbvevkb94c))
- we already computed the gradient of a plus b earlier so that we know how nding this
  sum will affect the output the question is what are individual gradients of A and B well intuitively if you nudge a by some amount a + b will be nudged by the same amount so the gradient or the partial derivative of the loss with respect to a is the same as the gradient of the sum and similarly for B ([View Highlight](https://read.readwise.io/read/01htcjjvvdc3efd0wb7b09df9y))
- when you encounter this situation in the compute graph then the gradient of the sum just simply propagates into the gradients of the nodes that plug into the sum machine ([View Highlight](https://read.readwise.io/read/01htcjm6fprcgrhhk6rp5sgyxp))
- multiplication node in the compute graph distributes the downstream gradient across incoming nodes by multiplying it cross Ways by their values ([View Highlight](https://read.readwise.io/read/01htcjnz5n4x5kfyyx323mpsez))
- similar rules can be easily formulated for other building block calculations such as raising a number to a power or taking the logarithm ([View Highlight](https://read.readwise.io/read/01htcjp91fd15rsd26920tj3x5))
- when a single node takes part in multiple branches of the
  compute graph gradients from the corresponding branches are simply added together ([View Highlight](https://read.readwise.io/read/01htcjprrvgemw2122e5364gef))
- the rightmost node in the graph is the resulting value of the loss function how does the incremental change in that node affect
  the output well it is the output so its gradient is by definition equal to one ([View Highlight](https://read.readwise.io/read/01htcjrej0cws2hbns6nq9yd95))
- the loss function is the sum of many Delta y's squared we know what to do with the summation node it just copies whatever the gradient value is to the right of it into all incoming nodes ([View Highlight](https://read.readwise.io/read/01htcjrt5wffp7z2nedzkj453d))
- we can keep doing this propagation of sequential derivative calculation backwards along our compute graph until we reach the leftmost nodes which are the data and parameter knobs ([View Highlight](https://read.readwise.io/read/01htcjva3g0e0x3pjj8c3c3fmd))
- derivatives with respect to the parameters is exactly what we want once these parameter gradients are found we can perform one iteration of gradient descent namely we're going to slightly tweak the knobs in the directions opposite to the gradient ([View Highlight](https://read.readwise.io/read/01htcjvzgjh1rcpfa9vd8hyp1h))
- magnitude of each adjustment being the negative product of the gradient and some small number called The Learning rate ([View Highlight](https://read.readwise.io/read/01htcjx6m5zxsd4m5d3x8rr7fq))
- configuration of the machine and the resulting loss are different and so the old gradient values we found no longer hold so we need to run the forward and backward calculations once again to obtain updated gradients and the new decreased loss performing this Loop of forward pass backward pass nudge repeat is the
  essence of training every modern machine Learning System and exactly the same algorithm is used today in even the most complicated models ([View Highlight](https://read.readwise.io/read/01htcjxg18x27vecj44ajqzash))
- The parameters for instance a feed forward neural network is essentially a
  bunch of multiplications and summations with a few nonlinear activation functions sprinkled between the layers each of those atomic computations is differentiable so you can construct the compute graph and run the backward path on it to find how each parameter like connection weights between neurons influence the loss function and because neural networks given enough neurons can in theory approximate any function imaginable we can create a large enough
  sequence of these building block mathematical machines to solve problems such as classifying images and even generating new text ([View Highlight](https://read.readwise.io/read/01htcjz51ajg8p0dtj505q9h7m))
