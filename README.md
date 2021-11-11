# [bmei-tarea-2] 


| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | 2 | 
| **TSR-2022-I** | Tarea *02* |
| **Robotica-2022-I**  | Tarea *02* |
| **IT102321-C002** | Sistema Ciber-Físico - Proyecto - Módulo |

## Contenido

- [Objetivo](#objetivo)
- [Introducción](#introduccion)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)

## Objetivo

Hacer que un robot móvil se mueva del punto A (0,0) al punto B (x,y) y en caso de detectar un obstáculo esquivarlo.

## Introducción

Investigación. Investigar los diferentes sensores que componen al robot Robotis Turtlebot3 Waffle y su transmisión de datos en ROS (nodos, tópicos, servicios, simulaciones).

### a) Sensores que componen al robot Robotis Turtlebot3 Waffle

**/gazebo/link_states** : Pública estados de todos los enlaces en simulación.

**/gazebo/model_states** : Pública estados de todos los modelos en simulación.

**/gazebo/parameter_descriptions** : Publica la descripción de los parámetros de los modelos de la simulación.

**/gazebo/parameter_updates** : Actualiza los nuevos parámetros de los modelos de la simulación.

**/gazebo/performance_metrics**: Publican un mensaje llamado que permite verificar el desempeño de cada sensor en el mundo.

**/gazebo/set_link_state**: Para probar la configuración de pose a través de temas.

**/gazebo/set_model_state** :Este servicio permite al usuario configurar las posiciones de las articulaciones del modelo sin invocar dinámicas.

**/imu** : Llama a la unidad de medición inercial.

**/joint_states**: Es un estado de un conjunto de juntas controladas por torque.

### b) Nodos
**/rosout**: Es un nodo para suscribirse, registrar y volver a publicar los mensajes.

**/recognizer/output**: Es un nodo de reconocimiento de voz.

**/gazebo**:Simulador de entornos 3D que posibilita evaluar el comportamiento de un robot en un mundo virtual

**/gazebo_gui**:Nodo que inicializa gazebo con roslaunch

**/robot_state_publisher**:Toma los ángulos de articulación del robot como entrada y publica las poses en 3D de los enlaces del robot, utilizando un modelo de árbol cinemático del robot

### c) Tópicos
**/camera/depth/camera_info** : Calibración y metadatos de la cámara.                                                                                          
**/camera/depth/image_raw** : Imagen sin procesar del dispositivo. Contiene profundidades uint16 en mm.

**/camera/depth/points** : Contiene una nube de puntos XYZ

**/camera/parameter_descriptions**: Es una imagen de descripciones de parámetros.

**/camera/parameter_updates**: Se usa para la actualizaciones de parámetros de una imagen.

**/camera/rgb/camera_info**: Calibración y metadatos de la cámara.

**/camera/rgb/image_raw**: Es una imagen sin procesar del dispositivo.

**/camera/rgb/image_raw/compressed**: Es una imagen sin procesar del dispositivo de forma comprimida.

**/camera/rgb/image_raw/compressed/parameter_descriptions**: Es una imagen sin procesar del dispositivo de forma comprimida de descripción de parámetros.

**/camera/rgb/image_raw/compressed/parameter_updates**: Se usa para la actualizaciones de parámetros de una imagen de forma comprimida.

**/clock**:Publicar tiempo de simulación, para ser utilizado con parámetro.

**/cmd_vel**: Se usa para controlar el giro a una velocidad.

**/odom**: Representa algo más que la "pose" del robot móvil ya que describe el estado "interno" del robot, es decir, la posición integrada utilizando codificadores de rueda y, potencialmente, con IMU fundida u otros sensores que miden el estado interno. A menudo, también se utiliza cuando se fusiona un sensor GNSS.

**/rosout_agg**: Es un feed agregado para suscribirse a los mensajes de registro de la consola. Este tema agregado se ofrece como una mejora del rendimiento.

**/scan** : Usa un escaneo único desde un telémetro láser plano.

**/tf** : Es un paquete que permite al usuario realizar un seguimiento de múltiples marcos de coordenadas a lo largo del tiempo.

### d) Servicios

**Servicios:Crea y destruye modelos en simulación.**
Estos servicios permiten al usuario generar y destruir modelos en simulación.

**~ / spawn_urdf_model ( gazebo_msgs / SpawnModel )**:Utilice este servicio para generar un modelo urdf .

**~ / spawn_gazebo_model ( gazebo_msgs / SpawnModel )**:Utilice este servicio para generar un modelo escrito en la descripción del modelo XML de Gazebo.

**~ / delete_model ( gazebo_msgs / DeleteModel )**: Este servicio permite al usuario eliminar un modelo de la simulación.

**Servicios: captadores de propiedades y del estado**.
Estos servicios permiten al usuario recuperar información sobre el estado y las propiedades de la simulación y los objetos en la simulación:

**~/get_model_properties**: - Este servicio devuelve las propiedades de un modelo en simulación.gazebo_msgs/GetModelProperties.

**~/get_model_state**: - Este servicio devuelve los estados de un modelo en simulación.gazebo_msgs/GetModelState.

**~/get_world_properties**: - Este servicio devuelve las propiedades del mundo de la simulación.gazebo_msgs/GetWorldProperties.

**~/get_joint_properties**: - Este servicio devuelve las propiedades de una articulación en simulación.gazebo_msgs/GetJointProperties.

**~/get_link_properties**: - Este servicio devuelve las propiedades de un enlace en simulación.gazebo_msgs/GetLinkProperties.

**~/get_link_state**: - Este servicio devuelve los estados de un enlace en simulación.gazebo_msgs/GetLinkState.

**~/get_physics_properties**: - Este servicio devuelve las propiedades del motor de física utilizado en la simulación.gazebo_msgs/GetPhysicsProperties.

**~/link_states**: - Publicar estados de enlace completos en el marco mundialgazebo_msgs/LinkStates.

**~/model_states**: - Publicar estados completos del modelo en el marco mundialgazebo_msgs/ModelStates.

**Servicios:Establecedores de estado y propiedades**
Estos servicios permiten al usuario establecer información de estado y propiedad sobre la simulación y los objetos en la simulación.

**~ / set_link_properties ( gazebo_msgs / SetLinkProperties )**:Este servicio establece las propiedades de un enlace en simulación.

**~ / set_physics_properties ( gazebo_msgs / SetPhysicsProperties )**:Este servicio permite al usuario establecer las propiedades de un enlace en la simulación.

**~ / set_model_state ( gazebo_msgs / SetModelState )**:Este servicio permite al usuario establecer las propiedades de un enlace en la simulación.

**~ / set_model_configuration ( gazebo_msgs / SetModelConfiguration )**:Este servicio permite al usuario establecer posiciones conjuntas del modelo sin invocar dinámicas.

**~ / set_joint_properties ( gazebo_msgs / SetJointProperties )**:Este servicio permite al usuario establecer las propiedades de un enlace en la simulación.

**~ / set_link_state ( gazebo_msgs / SetLinkState )**:Este servicio permite al usuario establecer las propiedades de un enlace en la simulación.

**Servicios:Control de simulación**
Estos servicios permiten al usuario pausar y reanudar la física en la simulación.

**~ / pause_physics ( std_srvs / Vacío )**:Pausar actualizaciones de física.

**~ / unpause_physics ( std_srvs / Vacío )**:Reanudar las actualizaciones de física.

**Servicios:Control de fuerza**
Estos servicios permiten al usuario aplicar llaves y fuerzas a cuerpos y juntas en simulación.

**~ / apply_body_wrench ( gazebo_msgs / ApplyBodyWrench )**:Aplique una llave inglesa a un cuerpo en simulación. Todas las llaves activas aplicadas al mismo cuerpo son acumulativas.

**~ / apply_joint_effort ( gazebo_msgs / ApplyJointEffort )**:Aplicar esfuerzo a una articulación en simulación. Todos los esfuerzos activos aplicados a la misma articulación son acumulativos.

**~ / clear_joint_forces ( gazebo_msgs / ClearJointForces )**:Esfuerzos aplicados claros a una articulación.

**~ / clear_body_wrenches ( gazebo_msgs / ClearBodyWrenches )**: Llave transparente aplicada a un cuerpo.

### e) Simulaciones

**Gazebo**:Gazebo es un simulador de entornos 3D que posibilita evaluar el comportamiento de un robot en un mundo virtual. Permite, entre muchas otras opciones, diseñar robots de forma personalizada, crear mundos virtuales usando sencillas herramientas CAD e importar modelos ya creados.
Además, es posible sincronizarlo con ROS de forma que los robots emulados publiquen la información de sus sensores en nodos, así como implementar una lógica y un control que dé ordenes al robot.Forma parte del bundle de ros "ros-kinetic-desktop-full", no obstante el robot que se usará como ejemplo no está integrado. El robot al que nos referimos es Turtlebot, un pequeño robot con una estructura montada sobre una base de Roomba y que integra sensores de odometría y una cámara RGB-D, entre otros.

**rviz**:Es una herramienta de visualización en 3D para aplicaciones de ROS. Proporciona una vista del modelo de robot, captura la información de los sensores del robot y reproduce los datos capturados. Puede mostrar datos de cámara, láseres y dispositivos 3D y 2D, como imágenes y nubes de puntos.
Para realizar las tareas que se indican a continuación, rviz debe estar abierto y conectado a un trabajo de simulación en ejecución. Puede abrir rviz desde la página Simulation jobs detail (Detalles de trabajos de simulación) de un trabajo de simulación en ejecución.

## Desarrollo

[![En el siguiente video se documentó el funcionamiento del programa](https://media.discordapp.net/attachments/891388181361082421/908212341571747860/ros-tarea-2.png)](https://youtu.be/SJAjYbJKV4k)
👆🏻 Dar clic en la imagen para ver el funcionamiento


1. Descargar el mundo de prueba
 [documento](/src/robot_comm/docs/document-template.md)
 
3.
4.
5.
6.
7.
vinculo a otro  en el repositorio (_ruta relativa_).

Imágenes

![Markdown Guide](/images/markdown-logo.png) Markdown Guide [Basic Syntax](https://www.markdownguide.org/basic-syntax/), [Extended Syntax](https://www.markdownguide.org/extended-syntax/)

Ejemplo de la estructura del directorios del repositorio: 

Proyecto de **ROS** con los directorios **adicionales** para almacenar **imágenes** y **documentos** referentes al **proyecto**.

**Nota:** La estructura mostrada representa -en su mayoría- a los directorios más usados dentro de un proyecto de **ROS**.

```text
 /home/ibarcenas/rosdev/bmei-tarea-2
├── build
│   ├── atomic_configure
│   │   ├── env.sh
│   │   ├── local_setup.bash
│   │   ├── local_setup.sh
│   │   ├── local_setup.zsh
│   │   ├── setup.bash
│   │   ├── setup.sh
│   │   ├── _setup_util.py
│   │   └── setup.zsh
│   ├── bin
│   ├── catkin
│   │   └── catkin_generated
│   │       └── version
│   │           └── package.cmake
│   ├── catkin_generated
│   │   ├── env_cached.sh
│   │   ├── generate_cached_setup.py
│   │   ├── installspace
│   │   │   ├── env.sh
│   │   │   ├── local_setup.bash
│   │   │   ├── local_setup.sh
│   │   │   ├── local_setup.zsh
│   │   │   ├── setup.bash
│   │   │   ├── setup.sh
│   │   │   ├── _setup_util.py
│   │   │   └── setup.zsh
│   │   ├── order_packages.cmake
│   │   ├── order_packages.py
│   │   ├── setup_cached.sh
│   │   └── stamps
│   │       └── Project
│   │           ├── interrogate_setup_dot_py.py.stamp
│   │           ├── order_packages.cmake.em.stamp
│   │           ├── package.xml.stamp
│   │           └── _setup_util.py.stamp
│   ├── CATKIN_IGNORE
│   ├── catkin_make.cache
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   │   ├── 3.16.3
│   │   │   ├── CMakeCCompiler.cmake
│   │   │   ├── CMakeCXXCompiler.cmake
│   │   │   ├── CMakeDetermineCompilerABI_C.bin
│   │   │   ├── CMakeDetermineCompilerABI_CXX.bin
│   │   │   ├── CMakeSystem.cmake
│   │   │   ├── CompilerIdC
│   │   │   │   ├── a.out
│   │   │   │   ├── CMakeCCompilerId.c
│   │   │   │   └── tmp
│   │   │   └── CompilerIdCXX
│   │   │       ├── a.out
│   │   │       ├── CMakeCXXCompilerId.cpp
│   │   │       └── tmp
│   │   ├── clean_test_results.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── cmake.check_cache
│   │   ├── CMakeDirectoryInformation.cmake
│   │   ├── CMakeError.log
│   │   ├── CMakeOutput.log
│   │   ├── CMakeRuleHashes.txt
│   │   ├── CMakeTmp
│   │   ├── download_extra_data.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── doxygen.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── Makefile2
│   │   ├── Makefile.cmake
│   │   ├── progress.marks
│   │   ├── run_tests.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── TargetDirectories.txt
│   │   └── tests.dir
│   │       ├── build.make
│   │       ├── cmake_clean.cmake
│   │       ├── DependInfo.cmake
│   │       └── progress.make
│   ├── cmake_install.cmake
│   ├── CTestConfiguration.ini
│   ├── CTestCustom.cmake
│   ├── CTestTestfile.cmake
│   ├── gtest
│   │   ├── CMakeFiles
│   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   └── progress.marks
│   │   ├── cmake_install.cmake
│   │   ├── CTestTestfile.cmake
│   │   ├── googlemock
│   │   │   ├── CMakeFiles
│   │   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   │   ├── gmock.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   ├── gmock_main.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   └── progress.marks
│   │   │   ├── cmake_install.cmake
│   │   │   ├── CTestTestfile.cmake
│   │   │   └── Makefile
│   │   ├── googletest
│   │   │   ├── CMakeFiles
│   │   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   │   ├── gtest.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   ├── gtest_main.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   └── progress.marks
│   │   │   ├── cmake_install.cmake
│   │   │   ├── CTestTestfile.cmake
│   │   │   └── Makefile
│   │   ├── lib
│   │   └── Makefile
│   ├── Makefile
│   ├── robot_comm
│   │   ├── catkin_generated
│   │   │   ├── installspace
│   │   │   │   ├── robot_commConfig.cmake
│   │   │   │   ├── robot_commConfig-version.cmake
│   │   │   │   └── robot_comm.pc
│   │   │   ├── ordered_paths.cmake
│   │   │   ├── package.cmake
│   │   │   ├── pkg.develspace.context.pc.py
│   │   │   ├── pkg.installspace.context.pc.py
│   │   │   └── stamps
│   │   │       └── robot_comm
│   │   │           ├── package.xml.stamp
│   │   │           └── pkg.pc.em.stamp
│   │   ├── CMakeFiles
│   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   ├── progress.marks
│   │   │   ├── std_msgs_generate_messages_cpp.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_eus.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_lisp.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_nodejs.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   └── std_msgs_generate_messages_py.dir
│   │   │       ├── build.make
│   │   │       ├── cmake_clean.cmake
│   │   │       ├── DependInfo.cmake
│   │   │       └── progress.make
│   │   ├── cmake_install.cmake
│   │   ├── CTestTestfile.cmake
│   │   └── Makefile
│   └── test_results
├── devel
│   ├── cmake.lock
│   ├── env.sh
│   ├── lib
│   │   └── pkgconfig
│   │       └── robot_comm.pc
│   ├── local_setup.bash
│   ├── local_setup.sh
│   ├── local_setup.zsh
│   ├── setup.bash
│   ├── setup.sh
│   ├── _setup_util.py
│   ├── setup.zsh
│   └── share
│       └── robot_comm
│           └── cmake
│               ├── robot_commConfig.cmake
│               └── robot_commConfig-version.cmake
├── README.md
└── src
    ├── CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake
    └── robot_comm
        ├── CMakeLists.txt
        ├── docs
        │   └── turtlebot3_obstacle_cube.world
        ├── images
        │   └── markdown-logo.png
        ├── package.xml
        └── src
            ├── go_to_goal.py
            ├── __init__.py
            ├── instructions.txt
            ├── logs.txt
            └── pub_sub.py

```

## Conclusiones

Conclusiones o cierre al trabajo realizado.



## Autor

| Iniciales  | Description |
| ----------:| ----------- |
| **BMEI** | Bárcenas Martínez Erick Iván [GitHub profile](https://github.com/erickbarcenas) |
| **NLA**  | Nieto Lara Aldo [GitHub profile](https://github.com/Aldomecatronic) |

## Referencias

<a id="3">[3]</a>  H.-L. Pham, V. Perdereau, B. Adorno, en P. Fraisse, “Position and Orientation Control of Robot Manipulators Using Dual Quaternion Feedback”, 11 2010, bll 658–663. <https://www.researchgate.net/publication/224200087_Position_and_Orientation_Control_of_Robot_Manipulators_Using_Dual_Quaternion_Feedback>

<https://moodle2018-19.ua.es/moodle/mod/book/view.php?id=8465&chapterid=181>

<https://docs.aws.amazon.com/es_es/robomaker/latest/dg/simulation-tools-rviz.html>

<https://wiki-ros-org.translate.goog/robot_state_publisher?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es-419&_x_tr_pto=nui,sc>

<https://wiki-ros-org.translate.goog/gazebo?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es-419&_x_tr_pto=nui,sc>


