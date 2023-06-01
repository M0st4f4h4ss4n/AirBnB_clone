<!DOCTYPE html>
<html>
<head>
  <style>
    body {
      background-color: #f1f1f1;
      font-family: Arial, sans-serif;
      margin: 0;
      padding: 20px;
    }
    h1 {
      color: #333;
      font-size: 32px;
      margin-bottom: 20px;
    }
p {
  color: #555;
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 10px;
}

pre {
  background-color: #fff;
  border: 1px solid #ddd;
  border-radius: 5px;
  padding: 10px;
}

code {
  font-family: Consolas, monospace;
}

.container {
  max-width: 800px;
  margin: 0 auto;
}

.emoji {
  font-size: 24px;
  margin-right: 5px;
}
  </style>
</head>
<body>
  <div class="container">
    <h1><span class="emoji">🏠</span> AirBnB Clone</h1>
    <p>
      This repository covers Part 1 & Part 2 of an AirBnB Clone project in Python/Flask.
    </p>

<p>
  The full-stack project is divided into 7 Parts:
</p>

<table>
  <tr>
    <th>Parts</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>1. Console</td>
    <td>Data model management via command interpreter</td>
  </tr>
  <tr>
    <td>2. Web static</td>
    <td>Landing page in HTML and CSS</td>
  </tr>
  <tr>
    <td>3. MySQL storage</td>
    <td>
      Migration of local file storage to MySQL database
    </td>
  </tr>
  <tr>
    <td>4. Deploy static</td>
    <td>
      Deploy web static on an Nginx server
    </td>
  </tr>
  <tr>
    <td>5. Web framework - templating</td>
    <td>Web server deployment with Flask</td>
  </tr>
  <tr>
    <td>6. RESTful API</td>
    <td>Creating endpoints for CRUD operations</td>
  </tr>
  <tr>
    <td>7. Web dynamic</td>
    <td>Loading of objects from client side using Jquery</td>
  </tr>
</table>

<p>
  <strong>Expected web static for the final product:</strong>
</p>

<img src="web_static_final.png" alt="Web Static Final" style="max-width: 100%">

<p>
  <strong>Web Stack for building the product:</strong>
</p>

<img src="web_stack.png" alt="Web Stack" style="max-width: 100%">

<p>
  <strong>Schemas:</strong>
</p>

<img src="schemas.png" alt="Schemas" style="max-width: 100%">

<h2><span class="emoji">💻</span> Part 1: AirBnB clone - The console</h2>

<p>
  Part 1 of AirBnB Clone project @Holberton: The goal of this project is to deploy a server with a simple copy of the AirBnB web app to demonstrate technical grasp (dare we say mastery?) of both front &amp; backend development.
</p>

<p>
  The overall Project scope is:
</p>

<ul>
  <li>Build a command line interpreter to manipulate data without a visual interface.</li>
  <li>A front-end (user interface) and a back-end for the web app: static and dynamic.</li>
  <li>Data storage via a database or a file storage.</li>
  <li>An API that bridges the front-end and the data (retrieve, create, delete, update).</li>
</ul>

<h3>Objectives For The BaseModel Class:</h3>

<p>
  A Class that defines all common attributes/methods for other classes:
</p>

<ul>
  <li><strong>Public instance attributes:</strong></li>
  <ul>
    <li><code>id:</code> string - assign with a UUID when an instance is created: you can use <code>uuid.uuid4()</code> to generate unique id but don’t forget to convert to a string the goal is to have unique id for each BaseModel</li>
    <li><code>created_at:</code> datetime - assign with the current datetime when an instance is created</li>
    <li><code>updated_at:</code> datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
  </ul>
  <li><strong>Public instance methods:</strong></li>
  <ul>
    <li><code>save(self):</code> updates the public instance attribute <code>updated_at</code> with the current datetime</li>
    <li><code>to_dict(self):</code> returns a dictionary containing all keys/values of dict of the instance:
      <ul>
        <li>by using <code>self.__dict__</code>, only instance attributes set will be returned</li>
        <li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
        <li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:
          <ul>
            <li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: 2017-06-14T22:31:03.285259)</li>
            <li>you can use <code>isoformat()</code> of datetime object</li>
          </ul>
        </li>
      </ul>
    </li>
  </ul>
</ul>

<h3>Objectives For The Command Line Interpreter:</h3>

<p>
  Create a new object (ex: a new User or a new Place), retrieve an object from a file, a database, etc., do operations on objects (count, compute stats, etc.), update attributes of an object, and destroy an object.
</p>

<h4>Operating In Interactive Mode:</h4>

<pre><code>
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
</code></pre>


<h4>Operating In Non-Interactive Mode:</h4>

<pre><code>
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
EOF help quit
(hbnb)
</code></pre>


<pre><code>
$ cat test_help
help
</code></pre>


<pre><code>
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
EOF help quit
(hbnb)
</code></pre>


<h4>Example Usage:</h4>

<pre><code>
newMod = BaseModel()

creates an instance of a method
print(NewMod.id)

prints the UUID
b6a6e15c-c67d-4312-9a75-9d084935e5
print(NewMod.created_at)

prints the time when the instance was created (ISO format)
'2017-09-28T21:03:54.052298'
print(NewMod.updated_at)

prints the most recent time that file was updated (ISO format)
'2017-09-28T21:03:54.052302'

</code></pre>

<h3>Directory Tree Structure For Phase #1 of HBnB Clone:</h3>

<pre><code>
.
├── AUTHORS
├── console.py
├── models
│ ├── amenity.py
│ ├── base_model.py
│ ├── city.py
│ ├── engine
│ │ ├── file_storage.py
│ │ ├── init.py
│ │ └── pycache
│ │ ├── file_storage.cpython-34.pyc
│ │ └── init.cpython-34.pyc
│ ├── init.py
│ ├── place.py
│ ├── pycache
│ │ ├── amenity.cpython-34.pyc
│ │ ├── base_model.cpython-34.pyc
│ │ ├── city.cpython-34.pyc
│ │ ├── init.cpython-34.pyc
│ │ ├── place.cpython-34.pyc
│ │ ├── review.cpython-34.pyc
│ │ ├── state.cpython-34.pyc
│ │ └── user.cpython-34.pyc
│ ├── review.py
│ ├── state.py
│ └── user.py
├── README.md
└── tests
└── test_models
├── init.py
├── pycache
│ ├── init.cpython-34.pyc
│ ├── test_amenity.cpython-34.pyc
│ ├── test_base_model.cpython-34.pyc
│ ├── test_city.cpython-34.pyc
│ ├── test_place.cpython-34.pyc
│ ├── test_review.cpython-34.pyc
│ ├── test_state.cpython-34.pyc
│ └── test_user.cpython-34.pyc
├── test_amenity.py
├── test_base_model.py
├── test_city.py
├── test_engine
│ ├── init.py
│ ├── pycache
│ │ ├── init.cpython-34.pyc
│ │ └── test_file_storage.cpython-34.pyc
│ └── test_file_storage.py
├── test_place.py
├── test_review.py
├── test_state.py
└── test_user.py
</code></pre>

<h2><span class="emoji">⚙️</span> Tasks</h2>

<h3>Console Tasks</h3>

<ol>
  <li>
    <strong>README, AUTHORS</strong>
    <p>Write a README.md</p>
  </li>
  <li>
    <strong>Be PEP8 compliant!</strong>
    <p>Write beautiful code that passes the PEP8 checks.</p>
  </li>
  <li>
    <strong>Unittests</strong>
    <p>All your files, classes, functions must be tested with unit tests.</p>
  </li>
  <li>
    <strong>BaseModel</strong>
    <p>
      Write a class BaseModel that defines all common attributes/methods for other classes:
    </p>
    <ul>
      <li>
        <strong>Public instance attributes:</strong>
        <ul>
          <li><code>id:</code> string - assign with a UUID when an instance is created: you can use <code>uuid.uuid4()</code> to generate unique id but don’t forget to convert to a string the goal is to have unique id for each BaseModel</li>
          <li><code>created_at:</code> datetime - assign with the current datetime when an instance is created</li>
          <li><code>updated_at:</code> datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object</li>
        </ul>
      </li>
      <li>
        <strong>Public instance methods:</strong>
        <ul>
          <li><code>save(self):</code> updates the public instance attribute <code>updated_at</code> with the current datetime</li>
          <li><code>to_dict(self):</code> returns a dictionary containing all keys/values of dict of the instance:
            <ul>
              <li>by using <code>self.__dict__</code>, only instance attributes set will be returned</li>
              <li>a key <code>__class__</code> must be added to this dictionary with the class name of the object</li>
              <li><code>created_at</code> and <code>updated_at</code> must be converted to string object in ISO format:
                <ul>
                  <li>format: <code>%Y-%m-%dT%H:%M:%S.%f</code> (ex: 2017-06-14T22:31:03.285259)</li>
                  <li>you can use <code>isoformat()</code> of datetime object</li>
                </ul>
              </li>
            </ul>
          </li>
        </ul>
      </li>
    </ul>
  </li>
  <li>
    <strong>Create BaseModel from dictionary</strong>
    <p>
      Update <code>models/base_model.py</code>:
    </p>
    <ul>
      <li><code>__init__(self, *args, **kwargs)</code>: you will use <code>*args</code>, <code>**kwargs</code> arguments for the constructor of a BaseModel.</li>
      <li>
        <strong>Note:</strong> created_at and updated_at are strings in this dictionary, but inside your BaseModel instance is working with datetime object. You have to convert these strings into datetime object. Tip: you know the string format of these datetime.
      </li>
    </ul>
  </li>
</ol>

<h2><span class="emoji">📝</span> Files</h2>

<table>
  <tr>
    <th>File Name</th>
    <th>Description</th>
  </tr>
  <tr>
    <td>README.md</td>
    <td>A description of the Holberton AirBnB Project</td>
  </tr>
  <tr>
    <td>AUTHORS</td>
    <td>A listing of the project contributors</td>
  </tr>
  <tr>
    <td>console.py</td>
    <td>The program to launch the HBNB console</td>
  </tr>
  <tr>
    <td>basemodel.py</td>
    <td>Defines the BaseModel Class</td>
  </tr>
  <tr>
    <td>file_storage.py</td>
    <td>Defines the FileStorage Class &amp; handles the database</td>
  </tr>
  <tr>
    <td>user.py</td>
    <td>Defines the User Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>city.py</td>
    <td>Defines the City Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>state.py</td>
    <td>Defines the User Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>amenity.py</td>
    <td>Defines the Amenity Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>review.py</td>
    <td>Defines the Review Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>place.py</td>
    <td>Defines the Place Class, a subclass of BaseModel</td>
  </tr>
  <tr>
    <td>tests/</td>
    <td>The test directory containing the unittest files for each Class</td>
  </tr>
</table>
  </div>
</body>
</html>
