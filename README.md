<h1 align="center"> Self-Driving Car Using Deep Learning (Quanser QCar)</h1>

<p align="center">
End-to-End Autonomous Navigation using CNN | Edge AI | Robotics
</p>

<p align="center">
  <img src="https://img.youtube.com/vi/D8EmFgQnPuM/0.jpg" width="500"/>
</p>

<hr/>

<h2>📌 Overview</h2>
<p>
This project presents an <b>end-to-end deep learning–based autonomous navigation system</b> 
developed using a <b>Convolutional Neural Network (CNN)</b> on the <b>Quanser QCar platform</b>.
</p>

<p>
The system enables a mobile robot to perform <b>real-time navigation and control directly from camera input</b>, 
eliminating the need for traditional rule-based pipelines.
</p>

<hr/>

<h2>🎯 Key Features</h2>
<ul>
  <li>🚀 End-to-end CNN-based autonomous driving pipeline</li>
  <li>🎥 Real-time object detection and navigation</li>
  <li>⚡ Direct mapping: Image → Velocity & Steering</li>
  <li>🧠 Edge deployment on NVIDIA Jetson TX2</li>
  <li>🤖 Tested on Quanser QCar hardware</li>
  <li>📦 Lightweight for embedded robotics applications</li>
</ul>

<hr/>

<h2>🧠 Methodology</h2>

<h3>🔹 Input</h3>
<ul>
  <li>Single-frame front-facing camera image</li>
</ul>

<h3>🔹 Model</h3>
<ul>
  <li>Convolutional Neural Network (CNN)</li>
  <li>Learns spatial features for navigation decisions</li>
</ul>

<h3>🔹 Output</h3>
<ul>
  <li>Linear Velocity</li>
  <li>Steering Angle</li>
</ul>

<p>
The model performs <b>end-to-end learning</b>, eliminating:
</p>
<ul>
  <li>Manual feature engineering</li>
  <li>Separate perception and control modules</li>
</ul>

<hr/>

<h2>⚙️ System Architecture</h2>

<p align="center">
<b>Camera Input → CNN Model → Control Commands → QCar Actuation</b>
</p>

<hr/>

<h2>📊 Results</h2>
<ul>
  <li>✅ Real-time autonomous navigation achieved</li>
  <li>🔄 Maximum turning angle: <b>30°</b></li>
  <li>📈 Stable velocity predictions across test scenarios</li>
</ul>

<p><b>Applications demonstrated:</b></p>
<ul>
  <li>Autonomous robots</li>
  <li>Smart mobility systems</li>
  <li>Edge AI deployments</li>
</ul>

<hr/>

<h2>🧪 Experimental Setup</h2>
<ul>
  <li><b>Platform:</b> Quanser QCar</li>
  <li><b>Compute:</b> NVIDIA Jetson TX2</li>
  <li><b>Language:</b> Python 3</li>
  <li><b>Framework:</b> TensorFlow Lite</li>
</ul>

<hr/>

<h2>📁 Project Structure</h2>

<pre>
Quanser/                          
Binary_classification_Train_Code.py
Hardware_Test_CSI_Camera_Single.py
Task_Self_Driving.py
classify.py
model.tflite
Datasets.zip
README.md
</pre>

<hr/>

<h2>🚀 Getting Started</h2>

<h3>1️⃣ Clone Repository</h3>
<pre>
git clone https://github.com/your-username/self-driving-qcar.git
cd self-driving-qcar
</pre>

<h3>2️⃣ Install Dependencies</h3>
<pre>
pip install -r requirements.txt
</pre>

<h3>3️⃣ Run Inference</h3>
<pre>
python Task_Self_Driving.py
</pre>

<hr/>

<h2>🎥 Demo</h2>
<p>
👉 <a href="#">[https://www.youtube.com/watch?v=D8EmFgQnPuM</a>
</p>

<hr/>

<h2>📌 Applications</h2>
<ul>
  <li>Autonomous mobile robots</li>
  <li>Warehouse automation (AGVs/AMRs)</li>
  <li>Smart navigation systems</li>
  <li>Edge AI robotics</li>
</ul>

<hr/>

<h2>🧩 Future Improvements</h2>
<ul>
  <li>🔗 Multi-sensor fusion (LiDAR + Camera)</li>
  <li>🌙 Robustness to lighting variations</li>
  <li>🎯 Multi-class object detection</li>
  <li>⚙️ ROS/ROS2 integration</li>
  <li>🚀 Upgrade to MobileNet / EfficientNet</li>
</ul>

<hr/>

<h2>🙌 Acknowledgments</h2>
<ul>
  <li>Quanser – QCar Platform</li>
  <li>NVIDIA – Jetson TX2</li>
  <li>Academic mentors and support</li>
</ul>

<hr/>

<h2>📬 Contact</h2>

<p>
<b>Muhammad Talha Ejaz</b><br/>
🔗 <a href="https://talhaejazh.github.io/">Portfolio</a><br/>
📝 <a href="https://medium.com/@talha.ej10">Blog</a>
</p>

<hr/>

<p align="center">
⭐ If you found this useful, consider giving it a star!
</p>
