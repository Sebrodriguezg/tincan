# Ondas longitudinales en un cilindro sólido rígido

En un **cilindro sólido y elástico**, las **ondas longitudinales** corresponden a oscilaciones de las partículas del material **en la misma dirección de la propagación**.  
A diferencia del caso acústico en un tubo (fluido), aquí el medio posee rigidez elástica caracterizada por su **módulo de Young** $E$, y la onda se propaga gracias a las deformaciones elásticas del sólido.

---

## 1. Descripción física

Cuando un extremo del cilindro es perturbado (por ejemplo, mediante una fuerza externa o una excitación mecánica), se generan compresiones y dilataciones sucesivas del material.  
Estas perturbaciones se propagan a lo largo del eje del cilindro $x$ en forma de **frentes de esfuerzo y deformación**, los cuales pueden considerarse planos si el radio del cilindro es pequeño respecto a la longitud de onda.

El desplazamiento longitudinal de las partículas se denota por $u(x,t)$, y está relacionado con la deformación uniaxial $\varepsilon = \partial u / \partial x$.  
El esfuerzo normal correspondiente se define como $\sigma = E\, \varepsilon$.

---

## 2. Ecuación de onda longitudinal

A partir de la segunda ley de Newton aplicada a un elemento diferencial del cilindro y la ley de Hooke para un sólido elástico, se obtiene la ecuación de movimiento:

$$
\rho \frac{\partial^2 u}{\partial t^2} = E \frac{\partial^2 u}{\partial x^2}.
$$

Esta es la **ecuación de onda longitudinal** en un medio elástico lineal y homogéneo.  
La velocidad de propagación de la onda se define como:

$$
c_L = \sqrt{\frac{E}{\rho}}.
$$

---

## 3. Ecuación con amortiguamiento y forzamiento externo

En la práctica, los materiales presentan pérdidas internas y pueden estar sometidos a una excitación externa.  
Para incluir estos efectos se añade un término de **amortiguamiento viscoso** proporcional a la velocidad de las partículas y una **fuerza forzante** $F(x,t)$:

$$
\rho \frac{\partial^2 u}{\partial t^2} + 2\alpha \rho \frac{\partial u}{\partial t}
    - E \frac{\partial^2 u}{\partial x^2} = F(x,t),
$$

donde:

- $\alpha$ es el coeficiente de amortiguamiento (s⁻¹),  
- $F(x,t)$ representa la densidad de fuerza aplicada (N/m³),  
- el término $2\alpha \rho \, \partial u / \partial t$ modela la disipación de energía mecánica en el material.

---

## 4. Condiciones de frontera

El cilindro puede presentar distintos tipos de condiciones de contorno:

- **Extremo fijo:** $u = 0$.  
- **Extremo libre:** $\partial u / \partial x = 0$ (sin esfuerzo).  
- **Acoplamiento con una fuente externa:** una fuerza mecánica aplicada o un pistón que impone un desplazamiento o presión en $x=0$.

---

## 5. Extensión tridimensional (modelo de onda plana)

Si el radio del cilindro es mucho menor que la longitud de onda ($R \ll \lambda$), la propagación puede considerarse **unidimensional** (onda plana) y el campo de desplazamiento $u(x,t)$ es aproximadamente uniforme sobre cada sección transversal.  
Esto permite estudiar el problema como una ecuación 1D efectiva, aunque el objeto sea tridimensional.

---

## 6. Objetivo del notebook

Este notebook se enfocará en:

1. Presentar la ecuación de onda longitudinal amortiguada y forzada en un cilindro rígido.  
2. Analizar cómo el módulo de Young $E$, la densidad $\rho$ y el amortiguamiento $\alpha$ afectan la propagación de las ondas.  
3. Servir como base para implementar un esquema numérico por diferencias finitas y visualizar el comportamiento del desplazamiento $u(x,t)$ y los frentes de esfuerzo.

---

> En resumen, este modelo describe la propagación longitudinal de deformaciones elásticas dentro de un cilindro rígido, considerando la elasticidad (módulo de Young), la inercia (densidad) y las pérdidas (amortiguamiento).



-----------





## Por qué la aproximación 1D es válida

La condición para que la aproximación 1D valga es $D \ll \lambda$, donde $\lambda$ es la longitud de onda en el material:
$$\lambda=\frac{c_L}{f},\qquad c_L=\sqrt{\frac{E}{\rho}}.$$

Para materiales metálicos típicos $c_L\sim 4{,}000$–$6{,}000\ \mathrm{m/s}$. Tomando $c_L\approx 5{,}000\ \mathrm{m/s}$ y la cota superior audible $f=20\ \text{kHz}$:
$$\lambda_{\min}\approx \frac{5,000}{20,000}=0.25\ \mathrm{m}.$$
Comparada con $D=1\ \mathrm{mm}=10^{-3}\ \mathrm{m}$, $\lambda_{\min}\gg D$ (factor $\sim 250$). Por tanto **no se excitan modos radiales relevantes** en el rango audible y el comportamiento axial se captura bien con un modelo 1D.

---

## Ecuación 1D útil para un cilindro con sección $A$

Si quieres incluir explícitamente el calibre (sección) en la relación fuerza–desplazamiento, la forma más directa es usar la ecuación para la **varilla/barra** (cantidad por unidad de longitud):

$$
\rho A \frac{\partial^2 u}{\partial t^2} + 2\alpha \rho A \frac{\partial u}{\partial t} - E A \frac{\partial^2 u}{\partial x^2} = F(x,t),
$$

donde:

* $A=\pi R^2$ (con $R=D/2$) es el área de la sección transversal,
* $\rho A$ es la masa por unidad de longitud,
* $E A$ aparece en el término de rigidez axial,
* $\alpha$ modela amortiguamiento estructural (s⁻¹),
* $F(x,t)$ es fuerza por unidad de longitud (N/m).

Si divides por $A$ vuelves a la forma en términos de densidad $\rho$:
$$
\rho \frac{\partial^2 u}{\partial t^2} + 2\alpha \rho \frac{\partial u}{\partial t} - E \frac{\partial^2 u}{\partial x^2} = \frac{F(x,t)}{A}.
$$

La velocidad de fase en la rama longitudinal fundamental sigue siendo
$$
c_L=\sqrt{\frac{E}{\rho}},
$$
es decir, el valor de $A$ modifica las magnitudes de fuerzas y energía pero **no** la velocidad básica $c_L$ en la teoría lineal básica.

---

## Supuestos que estás aceptando con el modelo 1D

* Desplazamientos pequeños (linealidad: ley de Hooke válida).
* Material homogéneo e isotrópico (o con propiedades efectivas constantes).
* Secciones transversales permanecen planas (Saint-Venant).
* No hay acoplamiento importante a modos flexionales o torsionales (válido si excitación es axial y radio muy pequeño).

Si alguno de estos no se cumple, habría que usar un modelo axisimétrico o 3D.

---

## Reglas numéricas prácticas para discretización (audible + D=1 mm)

Tomemos $c\approx 5{,}000\ \mathrm{m/s}$ y $f_{\max}=20\ \mathrm{kHz}$:

* Longitud de onda mínima: $\lambda_{\min}\approx 0.25\ \mathrm{m}$.
* Recomendación espacial: tomar paso espacial $dx \le \lambda_{\min}/10$ (regla práctica) → $dx \lesssim 0.025\ \mathrm{m}$.

  * Si tu cilindro mide, por ejemplo, $L=5\ \mathrm{m}$, entonces $N_x \approx 5/0.025 = 200$ puntos.
* Recomendación temporal (CFL y resolución temporal):

  * Condición CFL para esquema explícito: $c,dt/dx \le \text{CFL}_{\max}$ (usar $\text{CFL}\sim 0.8$–$0.95$).
  * Con $dx=0.025\ \mathrm{m}$ y $c=5{,}000\ \mathrm{m/s}$, elegir $dt \lesssim 0.9\cdot dx/c \approx 4.5\times 10^{-6}\ \mathrm{s}$.
  * También conviene que la frecuencia máxima esté bien muestreada: $f_s=1/dt \gtrsim 10 f_{\max}$ (regla práctica para buena representación), lo que da $dt \lesssim 5\times 10^{-6}\ \mathrm{s}$ — consistente con la CFL anterior.
* Si prefieres menos puntos en $x$, todavía puedes usar $dx\le \lambda/6$ para costos menores, pero cuidado con precisión de fase y amplitud.

---

## Condiciones de contorno y pérdidas prácticas

* Extremos **libres** reflejan con condición de esfuerzo nulo ($\partial u/\partial x =0$).
* Extremos **fijos**: $u=0$.
* Para evitar reflexiones en un tubo largo puedes añadir zonas amortiguantes (dashpots) o condiciones absorbentes aproximadas (términos de amortiguamiento local o “impedancia” en el extremo).
* Para pérdidas más físicas en metales, en vez de $2\alpha\rho$ puedes usar un módulo complejo efectivo $E^*(\omega)=E'( \omega)+\mathrm{i} E''(\omega)$ (viscoelasticidad) si necesitas modelar atenuación dependiente de frecuencia.

---

# Efecto de la tensión axial sobre la densidad efectiva del cilindro (área constante)

Consideremos un cilindro inicial de longitud $l_0$, área transversal constante $A_0$ y densidad volumétrica inicial $\rho_0$.  
Al aplicar una **tensión axial** $N$, el cilindro se **alarga** una cantidad $\Delta l$, de modo que la nueva longitud es:

$$
l = l_0(1 + \varepsilon), \qquad \varepsilon = \frac{\Delta l}{l_0}.
$$

El material se asume elástico lineal, por lo que la deformación y la tensión axial $\sigma$ se relacionan mediante el módulo de Young $E$:

$$
\sigma = E\,\varepsilon, \qquad \text{y como } \sigma = \frac{N}{A_0} \;\Rightarrow\; \varepsilon = \frac{N}{E A_0}.
$$

---

## Conservación de la masa

La masa total del cilindro permanece constante durante el estiramiento:

$$
m = \rho_0 A_0 l_0 = \rho(\varepsilon) A_0 l.
$$

De esta igualdad se obtiene la nueva densidad volumétrica:

$$
\rho(\varepsilon) = \frac{\rho_0}{1 + \varepsilon}.
$$

Físicamente, el alargamiento del cilindro corresponde a un **aumento en la distancia promedio entre las moléculas** del sólido, lo que reduce ligeramente la densidad efectiva del medio.

---

## Ecuación de onda longitudinal con densidad dependiente de la tensión

Tomando el área transversal constante y la nueva densidad $\rho(\varepsilon)$, la ecuación de onda longitudinal forzada y amortiguada en una dimensión queda:

$$
\rho(\varepsilon)\, \frac{\partial^2 u}{\partial t^2}
+ 2\alpha\, \rho(\varepsilon)\, \frac{\partial u}{\partial t}
- E\, \frac{\partial^2 u}{\partial x^2}
= f(x,t),
$$

donde:
- $u(x,t)$ es el desplazamiento axial,
- $\alpha$ es el coeficiente de amortiguamiento,
- $f(x,t)$ representa una fuerza externa por unidad de volumen.

Dividiendo toda la ecuación por $\rho(\varepsilon)$:

$$
\frac{\partial^2 u}{\partial t^2}
+ 2\alpha\, \frac{\partial u}{\partial t}
- c_N^2(\varepsilon)\, \frac{\partial^2 u}{\partial x^2}
= \frac{f(x,t)}{\rho(\varepsilon)},
$$

con la **velocidad de propagación dependiente de la tensión**:

$$
c_N(\varepsilon) = \sqrt{\frac{E}{\rho(\varepsilon)}}
= \sqrt{\frac{E}{\rho_0}\,(1 + \varepsilon)}.
$$

Usando $\varepsilon = N/(E A_0)$:

$$
c_N(N) = \sqrt{\frac{E}{\rho_0}\left(1 + \frac{N}{E A_0}\right)}.
$$

---

## Interpretación física

- A medida que el cilindro se estira, la densidad efectiva disminuye, lo que **aumenta la velocidad de propagación** de las ondas longitudinales.  
- El área transversal se mantiene constante, de modo que el cambio de velocidad depende únicamente de la variación de densidad debida a la elongación.  
- Para pequeñas deformaciones ($\varepsilon \ll 1$), puede aproximarse:

$$
c_N \approx c_0 \left(1 + \frac{\varepsilon}{2}\right), \qquad
c_0 = \sqrt{\frac{E}{\rho_0}}.
$$

Esta corrección es suficiente para describir el efecto de tensiones axiales moderadas en cilindros largos y delgados bajo frecuencias del espectro audible.

---

## Forma final simplificada

En resumen, bajo la hipótesis de área constante y tensión axial uniforme:

$$
\boxed{
\frac{\partial^2 u}{\partial t^2}
+ 2\alpha\,\frac{\partial u}{\partial t}
- \frac{E}{\rho_0}\,(1+\varepsilon)\,\frac{\partial^2 u}{\partial x^2}
= \frac{f(x,t)}{\rho_0/(1+\varepsilon)}
}
$$

donde $\varepsilon = N/(E A_0)$ describe la deformación elástica y el cambio asociado de densidad efectiva.


------------



## Construcción de la malla de simulación dependiente de la tensión

En la simulación de ondas longitudinales en un cilindro elástico, es necesario discretizar tanto el **espacio** como el **tiempo** para resolver numéricamente la ecuación de onda forzada y amortiguada.  
Sin embargo, en este modelo la **longitud efectiva del cilindro** cambia al aplicar una tensión axial, lo que implica que la **malla espacial también depende del estado de deformación**.

### 1. Longitud deformada

Sea $L_0$ la longitud inicial del cilindro y $\Delta L$ la elongación producida por una tensión axial $T$.  
Asumiendo un comportamiento lineal elástico (Ley de Hooke unidimensional), la deformación unitaria es:

$$
\varepsilon = \frac{\Delta L}{L_0} = \frac{T}{E A}
$$

donde:
- $E$ es el módulo de Young del material,
- $A$ el área transversal ($A = \pi D^2 / 4$),
- $T$ la tensión axial aplicada.

La nueva longitud total del cilindro será entonces:

$$
L = L_0 (1 + \varepsilon) = L_0 \left(1 + \frac{T}{E A}\right)
$$

Este valor $L$ define la extensión espacial de la malla sobre la que se resolverá la ecuación de onda.

---

### 2. Malla espacial

Se divide el dominio deformado $[0, L]$ en $N_x$ puntos espaciales equidistantes:

$$
x_i = i \, \Delta x, \quad \text{con} \quad \Delta x = \frac{L}{N_x - 1}, \quad i = 0, 1, \dots, N_x - 1
$$

La elección de $N_x$ dependerá de la resolución deseada y de la estabilidad numérica del esquema temporal (criterio de Courant).

---

### 3. Malla temporal

El paso temporal $\Delta t$ debe satisfacer la condición de estabilidad de Courant-Friedrichs-Lewy (CFL):

$$
c \frac{\Delta t}{\Delta x} \le 1
$$

donde la velocidad de propagación de la onda longitudinal está dada por:

$$
c = \sqrt{\frac{E}{\rho}}
$$

con $\rho$ la densidad efectiva del cilindro.  
Dado que la densidad depende de la elongación (disminuye al aumentar $L$), se toma:

$$
\rho = \rho_0 \frac{L_0}{L} = \rho_0 \frac{1}{1 + \frac{T}{E A}}
$$

De esta forma, tanto $c$ como $\rho$ se actualizan coherentemente con la tensión aplicada.

---

### 4. Resumen computacional

Para cada cuerda (material) y para cada tensión aplicada:
1. Se calcula el área $A$ y la longitud final $L$.
2. Se obtiene la densidad efectiva $\rho$ y la velocidad $c$.
3. Se construye una malla espacial `x` y temporal `t` adecuadas.
4. Estos valores se usarán posteriormente en el esquema numérico (por ejemplo, diferencias finitas explícitas) para simular la evolución temporal de la perturbación longitudinal.

----------


## Método numérico para la ecuación de onda longitudinal amortiguada y forzada
### Caso: tubo cilíndrico con extremo forzado y libre, excitado con un barrido de frecuencias

El sistema corresponde a un **tubo cilíndrico rígido** (aproximado unidimensionalmente) sometido a una **excitación longitudinal en un extremo ($x=0$)**, mientras que el otro extremo ($x=L$) permanece **libre**.  
El objetivo es estudiar la respuesta del sistema a un **barrido de frecuencias** que recorra el espectro audible humano, revelando los modos de resonancia y el comportamiento acústico dependiente del material y la tensión aplicada.

---

### 1. Ecuación de movimiento

La ecuación de onda longitudinal amortiguada y forzada es:

$$
\frac{\partial^2 u(x,t)}{\partial t^2}
+ \alpha \frac{\partial u(x,t)}{\partial t}
= c^2 \frac{\partial^2 u(x,t)}{\partial x^2} + f(x,t)
$$

donde:
- $u(x,t)$ es el desplazamiento longitudinal,
- $c = \sqrt{E / \rho_{\text{eff}}}$ es la velocidad efectiva de propagación,
- $\alpha$ representa las pérdidas internas del material,
- $f(x,t)$ es el término de excitación o fuerza externa.

---

### 2. Condiciones de frontera

1. **Extremo izquierdo (x = 0): forzado**  
   En este extremo se aplica una señal excitadora que realiza un **barrido temporal de frecuencias**:

   $$
   u(0,t) = A \sin\left( 2\pi f(t) \, t \right)
   $$

   donde $f(t)$ varía de manera continua entre dos valores:  
   $f_{\text{min}} = 20~\text{Hz}$ y $f_{\text{max}} = 20{,}000~\text{Hz}$.

   Este tipo de excitación (también conocida como *chirp* o *sweep*) permite observar la respuesta del tubo a todo el rango audible en una sola simulación.

   La función de barrido lineal en el tiempo puede definirse como:

   $$
   f(t) = f_{\text{min}} + (f_{\text{max}} - f_{\text{min}}) \frac{t}{t_{\text{max}}}
   $$

   o bien de manera exponencial, para mantener una tasa de cambio constante en escala logarítmica:

   $$
   f(t) = f_{\text{min}} \left( \frac{f_{\text{max}}}{f_{\text{min}}} \right)^{t/t_{\text{max}}}
   $$

2. **Extremo derecho (x = L): libre**  
   No hay fuerza neta en el borde:

   $$
   \frac{\partial u}{\partial x}\Big|_{x=L} = 0
   $$

   lo que en diferencias finitas equivale a:

   $$
   u_{N}^{n} = u_{N-1}^{n}
   $$

---

### 3. Discretización y esquema explícito

La ecuación se discretiza mediante el esquema explícito centrado en el tiempo y en el espacio:

$$
u_i^{n+1} =
(2 - \alpha \Delta t) u_i^n
- (1 - \alpha \Delta t) u_i^{n-1}
+ c^2 \left( \frac{(\Delta t)^2}{(\Delta x)^2} \right)
\left( u_{i+1}^n - 2u_i^n + u_{i-1}^n \right)
+ (\Delta t)^2 f_i^n
$$

con estabilidad garantizada por el criterio CFL:

$$
r = \frac{c \Delta t}{\Delta x} \le 1
$$

---

### 4. Condiciones iniciales

Inicialmente, el tubo se encuentra en reposo:

$$
u(x,0) = 0, \quad \frac{\partial u}{\partial t}(x,0) = 0
$$

---

### 5. Interpretación física

El barrido de frecuencias genera una excitación continua que:
- Explora todos los modos longitudinales de resonancia del tubo.
- Permite identificar las frecuencias naturales mediante la amplitud máxima de respuesta.
- Muestra cómo el amortiguamiento y la densidad efectiva afectan la propagación de ondas y las pérdidas de energía.

En el extremo libre ($x=L$), la onda se refleja **sin inversión de fase**, y la superposición con la onda incidente produce una distribución estacionaria dependiente de la frecuencia.

---

### 6. Procedimiento de simulación

1. Generar la malla dependiente de la tensión (usando `crear_malla()`).
2. Definir el barrido de frecuencia $f(t)$ y la excitación $u(0,t)$.
3. Aplicar condiciones de frontera: forzado en $x=0$, libre en $x=L$.
4. Resolver la ecuación con diferencias finitas explícitas.
5. Registrar la respuesta $u(x,t)$ o $u(L,t)$.
6. Analizar los resultados en el dominio del tiempo y de la frecuencia (por ejemplo, mediante FFT).

----------



## Método numérico: integración temporal con excitación de barrido de frecuencias

Para simular las ondas longitudinales en el tubo, se resuelve numéricamente la ecuación diferencial unidimensional:

$$
\frac{\partial^2 u(x,t)}{\partial t^2} = c^2(\sigma) \frac{\partial^2 u(x,t)}{\partial x^2} - \alpha \frac{\partial u(x,t)}{\partial t}
$$

donde:
- $u(x,t)$ es el desplazamiento longitudinal.
- $c(\sigma) = \sqrt{\frac{E}{\rho(\sigma)}}$ es la velocidad del sonido efectiva, dependiente de la tensión aplicada a través del cambio de densidad.
- $\alpha$ es el coeficiente de amortiguamiento.

El sistema físico se modela como un **tubo con un extremo forzado (x=0)** y **un extremo libre (x=L)**:
- En el extremo izquierdo se aplica una excitación temporal sinusoidal de frecuencia variable:
  $$
  u(0,t) = A_0 \sin\left( 2\pi f(t) t \right)
  $$
  donde $f(t)$ barre el espectro audible de 20 Hz a 20 kHz de manera lineal o logarítmica durante el tiempo total de simulación $T$.
- En el extremo derecho se cumple la condición de frontera libre:
  $$
  \frac{\partial u}{\partial x}\bigg|_{x=L} = 0
  $$

### Discretización numérica
Se usa el esquema explícito de diferencias finitas en el tiempo y espacio (método de las tres diagonales):

$$
u_i^{n+1} = (2 - \alpha \Delta t)u_i^n - (1 - \alpha \Delta t)u_i^{n-1} + \left( \frac{c \Delta t}{\Delta x} \right)^2 (u_{i+1}^n - 2u_i^n + u_{i-1}^n)
$$

donde:
- $\Delta x$ es el paso espacial definido por la malla generada para cada cuerda.
- $\Delta t$ se selecciona de acuerdo con la condición de estabilidad de Courant:
  $$
  \Delta t \le \frac{\Delta x}{c_{\text{max}}}
  $$
  con $c_{\text{max}}$ la velocidad máxima esperada.

### Procedimiento de simulación
1. Se define la malla espacial para una cuerda con longitud inicial $L_0$ y se calcula su nueva longitud $L$ bajo la tensión aplicada.
2. Se actualiza la densidad efectiva $\rho(\sigma)$ y con ello la velocidad de propagación $c(\sigma)$.
3. Se inicializa el campo de desplazamientos $u(x,t)$ con condiciones de reposo.
4. En cada paso temporal:
   - Se actualizan las posiciones según el esquema de diferencias finitas.
   - Se aplica la excitación sinusoidal de frecuencia variable en $x=0$.
   - Se mantiene la condición libre en $x=L$.
5. Se registra el desplazamiento o la velocidad en puntos específicos para analizar resonancias y respuesta espectral.

### Resultados esperados
- Se obtendrán las **resonancias naturales** del tubo como picos en la respuesta.
- El barrido de frecuencias permitirá observar las **frecuencias propias dependientes de la tensión aplicada**, ya que la elongación modifica tanto la longitud efectiva como la densidad.


-------------


## Cálculo de energía espectral en el extremo libre

Para cuantificar cuánta energía acústica se transmite y refleja dentro del tubo o cilindro, se introduce la **densidad espectral de potencia** en el extremo libre, obtenida a partir de la Transformada de Fourier del desplazamiento:

$$
S(f) = |U(f)|^2
$$

donde $U(f)$ es la transformada de Fourier del desplazamiento $u(L, t)$ en el extremo libre.

El **área espectral total** se calcula como:

$$
A_{\text{espectral}} = \int_0^{f_{\max}} S(f)\, df
$$

Este valor es proporcional a la **energía total transmitida** hacia el extremo libre durante el barrido de frecuencias, permitiendo comparar la eficiencia de propagación entre distintos materiales o tensiones.

En la práctica:
- Un **mayor valor de $A_{\text{espectral}}$** indica que el material o la tensión permite una mejor transmisión de energía acústica.
- Un **menor valor** refleja mayor amortiguamiento o menor acoplamiento con las frecuencias forzadas.

### Implementación y paralelización

Para optimizar el cálculo:
- Se paralelizan las simulaciones de diferentes cuerdas o tensiones usando la librería `joblib`.
- Cada proceso independiente ejecuta la simulación de una cuerda, obtiene su señal en el extremo libre y calcula su área espectral.
- Al final, los resultados se combinan en una tabla comparativa.

La paralelización es útil porque cada simulación es independiente, y puede distribuirse entre múltiples núcleos del procesador.


----------



## Eficiencia espectral normalizada

La **eficiencia de transmisión acústica** $\eta$ se define como la razón entre la energía espectral total en el extremo libre y la energía espectral total inyectada en el extremo forzado:

$$
\eta = \frac{A_{\text{salida}}}{A_{\text{entrada}}}
$$

donde:
- $A_{\text{salida}} = \int_0^{f_{\max}} |U_L(f)|^2 df$ es el área espectral medida en el extremo libre ($x = L$),
- $A_{\text{entrada}} = \int_0^{f_{\max}} |U_0(f)|^2 df$ corresponde al desplazamiento aplicado en el extremo forzado ($x = 0$).

Esta razón $\eta$ permite comparar materiales, tensiones o amortiguamientos de forma *normalizada*, sin depender de la amplitud absoluta de la fuente.

Interpretación:
- $\eta \approx 1$ → alta eficiencia de transmisión (baja disipación).
- $\eta \ll 1$ → el sistema atenúa o disipa gran parte de la energía antes de llegar al extremo libre.

La eficiencia puede verse como una medida de la *transparencia acústica* del cilindro ante excitaciones longitudinales.
