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


About
-----

TODO: What are the main topics this meeting is about?

The [compiled PDF](TODO) is in the LaTeX folder.


KIT-Style
---------
This one doesn't compile, as you need the KIT-Style (logos, layout,
color theme)

Please take a look at the presentation "Tutorenschulung" for further
information.
