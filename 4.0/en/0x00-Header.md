---
    title: |
        ![](../images/owasp_logo_1c_notext.png)  
        Application Security Verification Standard 4.0  
    subtitle: Final
    date: March 2019
    titlepage: true
    titlepage-rule-height: 0
    table-use-row-colors: true
    toc: true
    toc-own-page: true
    geometry: "left=2cm,right=2cm,top=1.5cm,bottom=3cm"
    fontfamily: sourcesanspro
    fontfamilyoptions: 
    - default
    
    header-includes: |
        \usepackage{fancyhdr, ragged2e}
        \fancyhead{}
        \lhead{\parbox[t]{0.6\textwidth}{\RaggedRight\rightmark\strut}}
        \rhead{\parbox[t]{0.6\textwidth}{\RaggedLeft\leftmark\strut}}
        \setlength{\headheight}{3\baselineskip}
        \pagestyle{fancy}
        \fancyfoot[CO,CE]{Application Security Verification Standard}
        \fancyfoot[LE,RO]{\thepage}
        \fancyfoot[rE,lO]{\includegraphics[height=0.6cm]{../images/owasp_logo_header.png}}
        \let\tableofcontentsORIG\tableofcontents
        \renewcommand\tableofcontents{
            \newpage
            \tableofcontentsORIG
            \clearpage}
        \hypersetup{colorlinks=false,
            allbordercolors={0 0 0},
            pdfborderstyle={/S/U/W 1}}
---

