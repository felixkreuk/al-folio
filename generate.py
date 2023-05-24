import jinja2
from jinja2 import Template

news = [
    ("fa-newspaper-o", "Our model AudioGen, which generates audio from textual descriptions got some attention from the media: [<a href='https://www.newscientist.com/article/2341416-metas-text-to-audio-ai-can-create-common-sounds-and-generate-music/' target='blank'>New Scientist</a>]."),
    ("fa-book", "Our research paper <a href='https://arxiv.org/pdf/2111.07402.pdf' target='blank'><em>Textless Speech Emotion Conversion using Decomposed and Discrete Representations</em></a> was accepted to EMNLP 2022!"),
    ("fa-microphone", "Our model AudioGen, was covered by Aleksa Gordić: [<a href='https://www.youtube.com/watch?v=RyIn-DxGF-c'>YouTube</a>]."),
    ("fa-book", "4 papers accapted to INTERSPEECH 2022! More details in publications section."),
    ("fa-book", "Our paper <a href='https://ieeexplore.ieee.org/document/9747953'><em>Speech Time-Scale Modification With GANs</em></a> was accapted to IEEE Signal Processing Letters 2022!"),
    ("fa-trophy", "Started as a full-time Research Engineer at Meta AI Research"),
    ("fa-microphone", "Invited talk at <a href='https://homepages.inf.ed.ac.uk/htang2/sigml/seminar/'>ISCA SIGML Seminar<a>, [<a href='https://www.youtube.com/watch?v=gk6thCWl_eE'>Video</a>]."),
]

papers = [
    {
        "title": "Textually Pretrained Speech Language Models",
        "authors": "Michael Hassid, Tal Remez, Tu Anh Nguyen, Itai Gat, Alexis Conneau, <u>Felix Kreuk</u>, Jade Copet, Alexandre Defossez, Gabriel Synnaeve, Emmanuel Dupoux, Roy Schwartz, Yossi Adi",
        "venue": "arXiv, 2023",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2305.13009.pdf",
            "Samples": "https://pages.cs.huji.ac.il/adiyoss-lab/twist/",
        },
        "year": 2023,
    },
    {
        "title": "AudioGen: Textually Guided Audio Generation",
        "authors": "<u>Felix Kreuk</u>, Gabriel Synnaeve, Adam Polyak, Uriel Singer, Alexandre Défossez, Jade Copet, Devi Parikh, Yaniv Taigman, Yossi Adi",
        "venue": "International Conference on Learning Representations (ICLR), 2023",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2209.15352.pdf",
            "Samples": "https://felixkreuk.github.io/text2audio_arxiv_samples/",
        },
        "year": 2023,
    },
    {
        "title": "Textless Speech Emotion Conversion using Decomposed and Discrete Representations",
        "authors": "<u>Felix Kreuk</u>, Adam Polyak, Jade Copet, Eugene Kharitonov, Tu-Anh Nguyen, Morgane Rivière, Wei-Ning Hsu, Abdelrahman Mohamed Emmanuel Dupoux, Yossi Adi",
        "venue": "Conference on Empirical Methods in Natural Language Processing (EMNLP), 2022",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2111.07402.pdf",
            "Code,": "https://github.com/facebookresearch/fairseq/tree/main/examples/emotion_conversion",
            "Samples,": "https://speechbot.github.io/emotion/",
            "Blog": "https://ai.facebook.com/blog/generating-chit-chat-including-laughs-yawns-ums-and-other-nonverbal-cues-from-raw-audio/",
        },
        "year": 2022,
    },
    {
        "title": "A Systematic Comparison of Phonetic Aware Techniques for Speech Enhancement",
        "authors": "Or Tal, Moshe Mandel, <u>Felix Kreuk</u>, Yossi Adi",
        "venue": "The 23rd Annual Conference of the International Speech Communication Association (Interspeech), 2022",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2206.11000.pdf",
            "Code": "https://github.com/slp-rl/SC-PhASE",
        },
        "year": 2022,
    },
    {
        "title": "Self-supervised Speaker Diarization",
        "authors": "Yehoshua Dissen, <u>Felix Kreuk</u>, Joseph Keshet",
        "venue": "The 23rd Annual Conference of the International Speech Communication Association (Interspeech), 2022",
        "links": {
            "PDF": "https://arxiv.org/pdf/2204.04166.pdf"
        },
        "year": 2022,
    },
    {
        "title": "Formant Estimation and Tracking using Probabilistic Heat-Maps",
        "authors": "Yossi Shrem, <u>Felix Kreuk</u>, Joseph Keshet",
        "venue": "The 23rd Annual Conference of the International Speech Communication Association (Interspeech), 2022",
        "links": {
            "PDF": "https://arxiv.org/pdf/2206.11632.pdf"
        },
        "year": 2022,
    },
    {
        "title": "Correcting Misproducted Speech using Spectrogram Inpainting",
        "authors": "Talia Ben-Simon, <u>Felix Kreuk</u>, Faten Awwad, Jacob T. Cohen, Joseph Keshet",
        "venue": "The 23rd Annual Conference of the International Speech Communication Association (Interspeech), 2022",
        "links": {
            "PDF": "https://arxiv.org/pdf/2204.03379.pdf"
        },
        "year": 2022,
    },
    {
        "title": "Speech Time-Scale Modification With GANs",
        "authors": "Eyal Cohen, <u>Felix Kreuk</u>, Joseph Keshet",
        "venue": "IEEE Signal Processing Letters, 2022",
        "links": {
            "PDF": "https://ieeexplore.ieee.org/document/9747953"
        },
        "year": 2022,
    },
    {
        "title": "Self-supervised contrastive learning for unsupervised phoneme segmentation",
        "authors": "<u>Felix Kreuk</u>, Joseph Keshet, Yossi Adi",
        "venue": "The 21st Annual Conference of the International Speech Communication Association (Interspeech), 2020",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2007.13465.pdf",
            "Code": "https://github.com/felixkreuk/UnsupSeg"
        },
        "year": 2020,
    },
    {
        "title": "Hide and Speak: Towards Deep Neural Networks for Speech Steganography",
        "authors": "<u>Felix Kreuk</u>, Yossi Adi, Bhiksha Raj, Rita Singh, Joseph Keshet",
        "venue": "The 21st Annual Conference of the International Speech Communication Association (Interspeech), 2020",
        "links": {
            "PDF,": "https://arxiv.org/pdf/1902.03083.pdf",
            "Samples,": "projects/steg/index.html",
            "Code": "https://github.com/felixkreuk/HideAndSpeak"
        },
        "year": 2020,
    },
    {
        "title": "A Causal View of Compositional Zero-Shot Recognition",
        "authors": "Yuval Atzmon, <u>Felix Kreuk</u>, Uri Shalit, Gal Chechik",
        "venue": "The 34th Annual Conference on Neural Information Processing Systems (NeurIPS), 2020",
        "links": {
            "PDF": "https://arxiv.org/pdf/2006.14610.pdf"
        },
        "year": 2020,
    },
    {
        "title": "Phoneme Boundary Detection using Learnable Segmental Features",
        "authors": "<u>Felix Kreuk</u>, Yaniv Sheena, Joseph Keshet, Yossi Adi",
        "venue": "IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP), 2020",
        "links": {
            "PDF,": "https://arxiv.org/pdf/2002.04992.pdf",
            "Code": "https://github.com/felixkreuk/SegFeat"
        },
        "year": 2020,
    },
    {
        "title": "Deceiving End-to-End Deep Learning Malware Detectors using Adversarial Examples",
        "authors": "<u>Felix Kreuk</u>, Assi Barak, Shir Aviv-Reuven, Moran Baruch, Benny Pinkas, Joseph Keshet",
        "venue": "Workshop track at 32nd Conference on Neural Information Processing Systems (NeurIPS), 2018",
        "links": {
            "PDF": "https://arxiv.org/pdf/1802.04528.pdf"
        },
        "year": 2018,
    },
    {
        "title": "Fooling End-to-end Speaker Verification by Adversarial Examples",
        "authors": "<u>Felix Kreuk</u>, Yossi Adi, Moustapha Cisse, Joseph Keshet",
        "venue": "IEEE International Conference in Acoustic, Speech and Signal Processing (ICASSP), 2018",
        "links": {
            "PDF": "https://arxiv.org/pdf/1801.03339.pdf"
        },
        "year": 2018,
    },
]

with open("index_template.html", "r") as f:
    site = Template(f.read())

site = site.render(news_list=news, papers=papers)

with open("index.html", "w") as f:
    f.write(site)
