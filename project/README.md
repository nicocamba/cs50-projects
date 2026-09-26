# Galicia's A*
#### Video Demo:  https://youtu.be/pJVprzWvFXU
#### Description:

### Introduction
The central objective of my project is to create a specialized web page designed exclusively for the residents of Galicia. This unique web page is intended to serve as a valuable tool, offering users the capability to effortlessly identify the shortest route between any two of the 20 largest populations within the region. It is imperative to clarify that the term "largest" does not necessarily connote the size of the cities; rather, it denotes the most densely populated areas within the picturesque region of Galicia.

### Functionallity

# User Interface

The user interface of the web page is thoughtfully divided into two main sections: "index" and "busqueda." Within the "index" page, users are presented with a user-friendly interface where they can select two populations from a comprehensive list. Upon making their selections, a simple click on the "search" button initiates a seamless redirection to the "busqueda" page.

# Algorithm Implementation

The backbone of the web page's functionality lies in the main.py file. Here, the A* algorithm is meticulously implemented to compute the shortest and most efficient path between the user-selected populations. The algorithm intricately utilizes the spatial coordinates meticulously stored in the datos.py file.

# Search Process

The search process is designed to be intuitive for users. By selecting two populations of interest and initiating the search by clicking the designated button, the A* algorithm seamlessly kicks in. Leveraging the spatial coordinates from datos.py, the algorithm effectively determines the optimal path between the chosen populations.

# Result Display

Upon the culmination of the search, users are automatically directed to the "busqueda" page. On this page, they are presented with a visual representation of the shortest path, accompanied by images depicting the initial and final populations. The images utilized on the "busqueda" page are systematically organized in the static folder.

# Experimental Files

To push the boundaries of functionality and explore diverse features, additional .py files were strategically introduced. These experimental files played a crucial role in testing various functionalities, ensuring that the web page is versatile and resilient in handling different scenarios.

### Challenges

Implementing the A* algorithm surfaced as one of the most intricate and challenging aspects of the project. This crucial phase demanded a meticulous approach to calculations, and debugging became an ongoing necessity to address and rectify any issues that surfaced.

Despite the seemingly straightforward nature of simultaneously working with dynamic Python and static HTML, the integration process introduced its own set of complexities. The need to harmonize these distinct languages posed challenges that required thoughtful solutions to ensure a cohesive, effective, and robust end product.


