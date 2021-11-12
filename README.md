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

**/gazebo/link_states** : Pública estados de todos los enlaces en simulación.

**/gazebo/model_states** : Pública estados de todos los modelos en simulación.

**/gazebo/parameter_descriptions** : Publica la descripción de los parámetros de los modelos de la simulación.

**/gazebo/parameter_updates** : Actualiza los nuevos parámetros de los modelos de la simulación.

**/gazebo/performance_metrics**: Publican un mensaje llamado que permite verificar el desempeño de cada sensor en el mundo.

**/gazebo/set_link_state**: Para probar la configuración de pose a través de temas.

**/gazebo/set_model_state** :Este servicio permite al usuario configurar las posiciones de las articulaciones del modelo sin invocar dinámicas.

**/imu** : Llama a la unidad de medición inercial.

**/joint_states**: Es un estado de un conjunto de juntas controladas por torque.

**/odom**: Representa algo más que la "pose" del robot móvil ya que describe el estado "interno" del robot, es decir, la posición integrada utilizando codificadores de rueda y, potencialmente, con IMU fundida u otros sensores que miden el estado interno. A menudo, también se utiliza cuando se fusiona un sensor GNSS.

**/recognizer/output**: Es un nodo de reconocimiento de voz.

**/rosout**: Es un nodo para suscribirse, registrar y volver a publicar los mensajes.

**/rosout_agg**: Es un feed agregado para suscribirse a los mensajes de registro de la consola. Este tema agregado se ofrece como una mejora del rendimiento.

**/scan** : Usa un escaneo único desde un telémetro láser plano.

**/tf** : Es un paquete que permite al usuario realizar un seguimiento de múltiples marcos de coordenadas a lo largo del tiempo.

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




## Desarrollo

[![En el siguiente video se documentó el funcionamiento del programa](https://media.discordapp.net/attachments/891388181361082421/908212341571747860/ros-tarea-2.png)](https://youtu.be/SJAjYbJKV4k)
👆🏻 Dar clic en la imagen para ver el funcionamiento


1. Descargar el [mundo de prueba](/src/robot_comm/docs/turtlebot3_obstacle_cube.world) y guardarlo en la carpeta correspondiente.
 

2. Abrir el archivo [go_to_goal](/src/robot_comm/src/go_to_goal.py) y en la línea 192 pasarle valores a la clase MoveRobot.
``` python
# Elegir una coordenada B que esté por detrás del cubo

# x: posición x
# y: posición y
# vel_fast: velocidad cuando el robot se mueve rápido
move_robot = MoveRobot(x=-2.0, y=7.0, vel_fast=1.5)

```

3. Guardar el archivo.

4. Asegurarse de que la carpeta de esté repositorio sea reconocida.
``` shell
source ~/rosdev/bmei-tarea-2/devel/setup.bash
```

5. Correr el siguiente comando:
``` shell
roslaunch turtlebot3_gazebo turtlebot3_any_world.launch
```

6. Correr el siguiente comando:
``` shell
roslaunch turtlebot3_gazebo turtlebot3_gazebo_rviz.launch
```


7. Correr el siguiente comando:
``` shell
rosrun robot_comm go_to_goal.py
```

8. Ver el video del funcionamiento del proyecto:
https://youtu.be/SJAjYbJKV4k 

La estructura del repositorio se muestra a continuación: 


```text
 /home/ibarcenas/rosdev/bmei-tarea-2
├── build
│   ├── atomic_configure
│   │   ├── env.sh
│   │   ├── local_setup.bash
│   │   ├── local_setup.sh
│   │   ├── local_setup.zsh
│   │   ├── setup.bash
│   │   ├── setup.sh
│   │   ├── _setup_util.py
│   │   └── setup.zsh
│   ├── bin
│   ├── catkin
│   │   └── catkin_generated
│   │       └── version
│   │           └── package.cmake
│   ├── catkin_generated
│   │   ├── env_cached.sh
│   │   ├── generate_cached_setup.py
│   │   ├── installspace
│   │   │   ├── env.sh
│   │   │   ├── local_setup.bash
│   │   │   ├── local_setup.sh
│   │   │   ├── local_setup.zsh
│   │   │   ├── setup.bash
│   │   │   ├── setup.sh
│   │   │   ├── _setup_util.py
│   │   │   └── setup.zsh
│   │   ├── order_packages.cmake
│   │   ├── order_packages.py
│   │   ├── setup_cached.sh
│   │   └── stamps
│   │       └── Project
│   │           ├── interrogate_setup_dot_py.py.stamp
│   │           ├── order_packages.cmake.em.stamp
│   │           ├── package.xml.stamp
│   │           └── _setup_util.py.stamp
│   ├── CATKIN_IGNORE
│   ├── catkin_make.cache
│   ├── CMakeCache.txt
│   ├── CMakeFiles
│   │   ├── 3.16.3
│   │   │   ├── CMakeCCompiler.cmake
│   │   │   ├── CMakeCXXCompiler.cmake
│   │   │   ├── CMakeDetermineCompilerABI_C.bin
│   │   │   ├── CMakeDetermineCompilerABI_CXX.bin
│   │   │   ├── CMakeSystem.cmake
│   │   │   ├── CompilerIdC
│   │   │   │   ├── a.out
│   │   │   │   ├── CMakeCCompilerId.c
│   │   │   │   └── tmp
│   │   │   └── CompilerIdCXX
│   │   │       ├── a.out
│   │   │       ├── CMakeCXXCompilerId.cpp
│   │   │       └── tmp
│   │   ├── clean_test_results.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── cmake.check_cache
│   │   ├── CMakeDirectoryInformation.cmake
│   │   ├── CMakeError.log
│   │   ├── CMakeOutput.log
│   │   ├── CMakeRuleHashes.txt
│   │   ├── CMakeTmp
│   │   ├── download_extra_data.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── doxygen.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── Makefile2
│   │   ├── Makefile.cmake
│   │   ├── progress.marks
│   │   ├── run_tests.dir
│   │   │   ├── build.make
│   │   │   ├── cmake_clean.cmake
│   │   │   ├── DependInfo.cmake
│   │   │   └── progress.make
│   │   ├── TargetDirectories.txt
│   │   └── tests.dir
│   │       ├── build.make
│   │       ├── cmake_clean.cmake
│   │       ├── DependInfo.cmake
│   │       └── progress.make
│   ├── cmake_install.cmake
│   ├── CTestConfiguration.ini
│   ├── CTestCustom.cmake
│   ├── CTestTestfile.cmake
│   ├── gtest
│   │   ├── CMakeFiles
│   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   └── progress.marks
│   │   ├── cmake_install.cmake
│   │   ├── CTestTestfile.cmake
│   │   ├── googlemock
│   │   │   ├── CMakeFiles
│   │   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   │   ├── gmock.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   ├── gmock_main.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   └── progress.marks
│   │   │   ├── cmake_install.cmake
│   │   │   ├── CTestTestfile.cmake
│   │   │   └── Makefile
│   │   ├── googletest
│   │   │   ├── CMakeFiles
│   │   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   │   ├── gtest.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   ├── gtest_main.dir
│   │   │   │   │   ├── build.make
│   │   │   │   │   ├── cmake_clean.cmake
│   │   │   │   │   ├── DependInfo.cmake
│   │   │   │   │   ├── depend.make
│   │   │   │   │   ├── flags.make
│   │   │   │   │   ├── link.txt
│   │   │   │   │   ├── progress.make
│   │   │   │   │   └── src
│   │   │   │   └── progress.marks
│   │   │   ├── cmake_install.cmake
│   │   │   ├── CTestTestfile.cmake
│   │   │   └── Makefile
│   │   ├── lib
│   │   └── Makefile
│   ├── Makefile
│   ├── robot_comm
│   │   ├── catkin_generated
│   │   │   ├── installspace
│   │   │   │   ├── robot_commConfig.cmake
│   │   │   │   ├── robot_commConfig-version.cmake
│   │   │   │   └── robot_comm.pc
│   │   │   ├── ordered_paths.cmake
│   │   │   ├── package.cmake
│   │   │   ├── pkg.develspace.context.pc.py
│   │   │   ├── pkg.installspace.context.pc.py
│   │   │   └── stamps
│   │   │       └── robot_comm
│   │   │           ├── package.xml.stamp
│   │   │           └── pkg.pc.em.stamp
│   │   ├── CMakeFiles
│   │   │   ├── CMakeDirectoryInformation.cmake
│   │   │   ├── progress.marks
│   │   │   ├── std_msgs_generate_messages_cpp.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_eus.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_lisp.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   ├── std_msgs_generate_messages_nodejs.dir
│   │   │   │   ├── build.make
│   │   │   │   ├── cmake_clean.cmake
│   │   │   │   ├── DependInfo.cmake
│   │   │   │   └── progress.make
│   │   │   └── std_msgs_generate_messages_py.dir
│   │   │       ├── build.make
│   │   │       ├── cmake_clean.cmake
│   │   │       ├── DependInfo.cmake
│   │   │       └── progress.make
│   │   ├── cmake_install.cmake
│   │   ├── CTestTestfile.cmake
│   │   └── Makefile
│   └── test_results
├── devel
│   ├── cmake.lock
│   ├── env.sh
│   ├── lib
│   │   └── pkgconfig
│   │       └── robot_comm.pc
│   ├── local_setup.bash
│   ├── local_setup.sh
│   ├── local_setup.zsh
│   ├── setup.bash
│   ├── setup.sh
│   ├── _setup_util.py
│   ├── setup.zsh
│   └── share
│       └── robot_comm
│           └── cmake
│               ├── robot_commConfig.cmake
│               └── robot_commConfig-version.cmake
├── README.md
└── src
    ├── CMakeLists.txt -> /opt/ros/noetic/share/catkin/cmake/toplevel.cmake
    └── robot_comm
        ├── CMakeLists.txt
        ├── docs
        │   └── turtlebot3_obstacle_cube.world
        ├── images
        │   └── markdown-logo.png
        ├── package.xml
        └── src
            ├── go_to_goal.py
            ├── __init__.py
            ├── instructions.txt
            ├── logs.txt
            └── pub_sub.py

```

## Conclusiones

El robot tiene un ángulo de movimiento el cual le permite ir de un punto A a un punto B, ahora bien, como el robot
solo tiene dos ruedas se desvía y nuevamente debe de volverse a orientar. Si el robot tuviese cuatro ruedas el ir de un punto A a un punto B sería más rápido.

El robot tiene un láser el cual detecta si hay un objeto cerca, sin el láser este proyecto no se ubiese cumplido cabalmente pues el robot hubiese
chocado infinidas de veces con el objeto.

El conocer el robot es muy útil para saber qué sensor utilizar:

1. Se listan los tópicos:
``` shell
rostopic list
```
2. Se elije uno de interés:

``` shell
...
/odom
/scan
...
```

3. Se muestran su contenido:

``` shell
rostopic echo /scan

---
header: 
  seq: 1929
  stamp: 
    secs: 411
    nsecs: 531000000
  frame_id: "base_scan"
angle_min: 0.0
angle_max: 6.28318977355957
angle_increment: 0.017501922324299812
time_increment: 0.0
scan_time: 0.0
range_min: 0.11999999731779099
range_max: 3.5
ranges: [inf, inf, inf]
intensities: [0.0, 0.0, 0.0]
```

4. Se muestran su contenido:

``` shell
rostopic echo /odom -n1

---
header: 
  seq: 109463
  stamp: 
    secs: 3796
    nsecs: 665000000
  frame_id: "odom"
child_frame_id: "base_footprint"
pose: 
  pose: 
    position: 
      x: -2.0319656776671478
      y: 6.963572901438072
      z: -0.0010091347519655472
    orientation: 
      x: 0.0012717047342619566
      y: -0.0009628094662041425
      z: -0.7970080559829353
      w: -0.6039665673390399
  covariance: [1e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1000000000000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.001]
twist: 
  twist: 
    linear: 
      x: 1.3699118330504703e-06
      y: 3.4590369010973492e-06
      z: 0.0
    angular: 
      x: 0.0
      y: 0.0
      z: 2.356958725366544e-05
  covariance: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
---
```

5. Se muestran su contenido:

``` shell
rosmsg show Odometry

---
[nav_msgs/Odometry]:
std_msgs/Header header
  uint32 seq
  time stamp
  string frame_id
string child_frame_id
geometry_msgs/PoseWithCovariance pose
  geometry_msgs/Pose pose
    geometry_msgs/Point position
      float64 x
      float64 y
      float64 z
    geometry_msgs/Quaternion orientation
      float64 x
      float64 y
      float64 z
      float64 w
  float64[36] covariance
geometry_msgs/TwistWithCovariance twist
  geometry_msgs/Twist twist
    geometry_msgs/Vector3 linear
      float64 x
      float64 y
      float64 z
    geometry_msgs/Vector3 angular
      float64 x
      float64 y
      float64 z
  float64[36] covariance
```





## Autor

| Iniciales  | Description |
| ----------:| ----------- |
| **BMEI** | Bárcenas Martínez Erick Iván [GitHub profile](https://github.com/erickbarcenas) |
| **NLA**  | Nieto Lara Aldo [GitHub profile](https://github.com/Aldomecatronic) |

## Referencias

<a id="1">[1]	“ROS Developers LIVE Class #78: How to read laserscan data,” 17-Dec-2019. [En línea]. Disponible en: https://www.youtube.com/watch?v=Oal-aKJoC_U. [Recuperado: 11-Nov-2021].

<a id="2">[2]</a>  H.-L. Pham, V. Perdereau, B. Adorno, en P. Fraisse, “Position and Orientation Control of Robot Manipulators Using Dual Quaternion Feedback”, 11 2010, bll 658–663. <https://www.researchgate.net/publication/224200087_Position_and_Orientation_Control_of_Robot_Manipulators_Using_Dual_Quaternion_Feedback>

Manual de ROS: Simulador 3D Gazebo. (n.d.). Moodle2018-19.Ua.Es. Retrieved November 11, 2021, from <https://moodle2018-19.ua.es/moodle/mod/book/view.php?id=8465&chapterid=181>

(N.d.). Amazon.Com. Retrieved November 11, 2021, from <https://docs.aws.amazon.com/es_es/robomaker/latest/dg/simulation-tools-rviz.html>

robot_state_publisher - ROS Wiki. (n.d.). Translate.Goog. Retrieved November 11, 2021, from <https://wiki-ros-org.translate.goog/robot_state_publisher?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es-419&_x_tr_pto=nui,sc>

gazebo - ROS Wiki. (n.d.). Translate.Goog. Retrieved November 11, 2021, from <https://wiki-ros-org.translate.goog/gazebo?_x_tr_sch=http&_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es-419&_x_tr_pto=nui,sc>
