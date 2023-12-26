# OpenCV Nedir?
<b>OpenCV veya Open Source Computer Vision</b>, sahip olduğumuz resim ve videolarla çalışırken büyük katkıda destek sağlayacak bir kütüphanedir. Görüntü işleme, bilgisayar görüşü ve makine öğrenimi için geniş bir <b><i>işlevsellik yelpazesi sağlayan açık kaynaklı kodlardır</i></b>. OpenCV ilk olarak 1999 da <b>intel</b> tarafından kullanıma açıldı.

<div style="display: flex;">
  <img src="https://miro.medium.com/v2/resize:fit:875/0*Zs2vmh1zXm1aAQGk.jpg" title="Java" heigh=700 width=500 align="right" />
  <div style="text-align: left;">
    Bilgisayarlı görünün amacı dışarıdaki nesneleri anlamaktır, <b><i>bilgisayar anlayabilmek için karmaşık algoritma ve kodları kullanır</i></b>.

Bilgisayarlı görünün artık hayatımızın her noktasına girmiş bulunmaktadır örnek olarak yüz algılama teknolojisi, kişinin yüzünü algılar ve bu yüzleri sınıflandırmaya çalışır.

Kullanılan diğer alanlardan biri de gözetim alanındadır, kullanılış amacı güvenlik kısmı için daha çok kullanılır kişinin hareketlerini incelenir ve olası tahminleri bilgisayar ortamında tahmin edilir.

OpenCV (Open Source Computer Vision) <b>açık kaynaklı bir kod kütüphanesidir</b> ve herkese açık olarak kullanılabilmektedir. Algılama ve tanıma olarak ikiye ayıralım bu ikisi birbirine karıştırılan terimler, algılama dışarıdan veya resimdeki kişinin ne olduğunu anlamaktır algılamak ise resimde gördüğü bu kişinin kim olduğunu anlama kısmıdır.

<b><i>C++ dili kullanılarak geliştirilmiş bir kütüphanedir</i></b> ama istenilen diller ile de kullanılabilir ama son yıllarda yoğun olarak kullanılmaya başlayan python ile devam ediyorum.
  </div>
</div>

<img src="Soruce/771c275d-6c24-43c8-83e4-644f8341646e_1_Y1S4hciQTfrB3xJuk2remA已去底.png" title="Python&OpenCV" heigh ="1200" width="900"/>

# Computer Vision Terms
Bilgisayarlı görüdeki temel olarak kullanılan kavramlar;
<ul>
    <li><a href="https://klein.mathunion.org/matrices-and-digital-images/">Image Processing</a></li>
        <ul> 
            <li>Cihazın dışarıda gördüğü şeylerin gördüğü nesnelerin ne olduğunu anlamaya çalışması yani aldığı görsel verileri işlemesidir.</li>
            <li>Görüntü işleme bir matematiksel işlemdir, bilgisayarda görüntüler bir matris olarak algılanır nxn boyutunda bir matris şeklinde algılanır. Resmin derinliği varsa daha da farklı matematiksel yöntemlere gidilir.</li>
            <br>
             <figure>
              <img src="https://github.com/TriTetra/openCV_Examples/blob/main/Soruce/sample-matrix.gif" alt="Figure:2" heigh ="1200" width="900">
              <figcaption>Figure 2: The matrix corresponding to Felix The Cat</figcaption>
              </figure>
            <br><br>
            <figure>
              <img src="https://github.com/TriTetra/openCV_Examples/blob/main/Soruce/felix_the_cat_.png" alt="Figure:4" heigh ="1200" width="900">
              <figcaption>Figure 4: Matrix transformations</figcaption>
              </figure>
            <br><br>
           <li>Yukarıda gördüğünüz resimdeki kedi felix 35x35 matris (pixel) kullanılarak ortaya çıkarılmıştır, ekrandaki siyah noktalar 1’i beyaz noktalar da 0’ı ifade ederler. </li>
           <li>Figure 4’te saat yönünde x derece döndürdüğümüzde bize basit bir eylem gibi gelsede bilgisayarda bir matrisi döndürmemiz gerekir, bu işlemi yapmak içinde matrisin transpozu alınır veya gerekli yöntemler ile istenilen şekle gelene kadar işlem devam eder.</li>
        </ul>
</ul>



