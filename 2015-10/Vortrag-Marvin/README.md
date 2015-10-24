Organization
------------

* (TODO: Date and time of start)
* (TODO: Where)
* Language: German

About
-----

Der Vortrag dient als Auftakt zu einer *Paper Diskussion Group* zum Thema *Deep Learning und Pixelweise Klassifikation*. In diesem Bereich passiert aktuell extrem viel. Eine neue Veröffentlichung hierzu hat auf der *CVPR 2015* den *Best Paper Award* gewonnen und wurde in der kurzen Zeit bereits 90 mal zitiert. Dieses Paper ist Auftakt zu rasanter Entwicklung in diesem Bereich. Aktuell wird bei der Pixelweise Klassifikation versucht auf den Erfolgen von CNNs bei klassichen Klassifikationsproblemen wie MNIST und ImageNet aufzubauen. Derzeit zeichnen sich zwei interessante Ansätze ab:

1) **Sliding Window im Netz [2]**: Das Netz wird von der Architektur so entworfen, dass es ein Sliding-Window nachahmt. Auf diese Weise werden redundante Berechnungen des klassischen Sliding-Window Ansatzes Vermieden.

2) **Deconvolution Layer [1],[3]**: Die Faltungen des CNNs werden (approximativ) Rückgängig gemacht. Auf diese Weise erhält man Informationen, welche Bereiche und Pixel für die Klassifikation ausschlaggebend sind und kann dies zur Pixelweisen Klassifikation verwenden.

In der *Paper Discussion Group* möchten wir uns mit den neuesten Entwicklungen auf dem Gebiet der *Pixelweise Klassifikation* vertiefend auseinandersetzen. 


Paper Discussion Group
-----






Quellen
-----

[1] Fully Convolutional Networks for Semantic Segmentation; *Jon Long*, *Evan Shelhamer* **(CVPR 2015)**
[2] Efficient Convolutional Neural Networks for Pixelwise Classification on Heterogeneous Hardware Systems; *Fabian Tschopp* **(ETH 2015)**
[3] Deep Deconvolutional Networks for Scene Parsing; *Rahul Mohan* **(2014)**
[4] Pixel-wise Segmentation of Street with Neural Networks; *Martin Thoma*, *Marvin Teichmann et al.* **(2015)**


KIT-Style
---------
This one doesn't compile, as you need the KIT-Style (logos, layout,
color theme)

Please take a look at the presentation "Tutorenschulung" for further
information.
