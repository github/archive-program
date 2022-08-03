GitHub Arctic Code Vault: Tech Tree
===================================

## Introduction: A Guide To The Tech Tree

What follows, which we call the Tech Tree, is a selection of works intended to describe how the world makes and uses software today, as well as an overview of how computers work and the foundational technologies required to make and use computers. The purpose of the GitHub Archive Program is to preserve open source software for future generations. This implies also preserving the knowledge of other technologies on which open-source software runs, along with a depiction of the open-source movement which brought this software into being.

This initial version of the Tech Tree will consist almost entirely of copies of pre-existing works, none of which were written for an unknown audience a long way into the future. As such it is not so much a guide as a collection of resources that we hope will be historically interesting and/or useful. We have tried to strike a balance between abstract/theoretical and concrete/practical work, and to provide at least an overview of the entire technical stack on which modern software engineering rests.

In addition to this technical documentation, we have also included a selection of artistic, cultural, and historical works, to help describe the overall cultural context in which this archive was created. A data dump of an entire 2020 snapshot of Wikipedia in the archive's five primary languages, along with a snapshot of Stack Overflow and sundry other smaller data collections, is also stored alongside the works itemized below.

The current iteration of the Tech Tree is loosely divided into the following thirteen sections:

1. [_Fundamentals of computing and the Internet:_](#fundamentals-of-computing-and-the-internet) the essentials of how computers work, and, at least as important to today&#39;s world, how they are connected together into a single planetary network which includes most of the computers on Earth.
2. [_Algorithms and data structures:_](#algorithms-and-data-structures) processes, sets of rules, and methods of arranging data to solve common categories of problems in efficient ways. Metaphorically, algorithms are the intelligence in a software program, and data structures are its storage.
3. [_Compilers, assembler, and operating systems:_](#compilers-assembler-and-operating-systems) how written source code becomes the machine code which causes the electrical signals inside a computer to change in a controlled manner, and the theory of operating systems, the software which supports a computer&#39;s basic functions and provides the fundamental, low-level functionality that all other software ultimately calls upon.
4. [_Programming languages:_](#programming-languages) some of the world&#39;s most popular and widely used programming languages described in detail. While, fundamentally, any program can be written in any language, certain languages are better or worse at particular tasks.
5. [_Networking and connectivity:_](#networking-and-connectivity) how computers connect to one another, via physical wires and radio signals, both one-on-one and in larger networks. Includes descriptions of the structure of the global &quot;network of networks&quot; known as the Internet, which connects most of the computers on Earth.
6. [_Modern software development:_](#modern-software-development) the processes and procedures of dealing with software projects, tools, and services at scale, with constant monitoring and communication, at assured levels of quality.
7. [_Modern software applications:_](#modern-software-applications) in-depth description of applications such as Web development (the Web is, essentially, that part of the Internet used to display output and receive input from human beings); scientific research and analysis; image processing; pattern recognition and generation via neural networks; software distributed across many different computers; cryptocurrencies, which can be used as a platform for trustless decentralized software; and the new field of quantum computing.
8. [_Hardware architectures:_](#hardware-architectures) the concepts, structures, and layout of computer hardware. Hardware refers to physical electronic components; hardware architecture refers to how those components are structured and connected in order to run software; and software ultimately becomes ephemeral patterns of electricity within those physical components.
9. [_Hardware development:_](#hardware-development) how to build simple computers from collections of electronic components.
10. [_Electronic components, transistors, semiconductor manufacturing:_](#electronic-components-transistors-semiconductor-manufacturing) those electronic components which predated computers, along with individual transistors, the component from which computers are made, and an overview of the technologies and processes of fabricating interconnected transistors at scale.
11. [_Pre-industrial technologies:_](#pre-industrial-technologies) technologies of eras which predated electricity.
12. [_Fiction, culture, and history:_](#fiction-culture-and-history) human histories and changing human cultures, mostly through the lens of celebrated fictional narratives written over the last 150 years.
13. [_Cultural context:_](#cultural-context) information about humanity at the time the Tech Tree was created; in particular, a snapshot of Wikipedia, a collectively generated repository of all sorts of information about our world. Due to Wikipedia&#39;s enormous size, this section is provided as encoded data, like the rest of the archive, rather than as visual/readable pages.

The first seven sections are devoted to software, the purpose and content of the GitHub Arctic Code Vault, and its uses and applications. The next four sections describe the technologies required to construct computers on which software might run. The remaining two are intended to illustrate the human context in which these technologies have been developed, the stories the cultures of our era told, the languages in which we told them, and the factual background and descriptions of the world in which we lived.

The Tech Tree is part of the much larger GitHub Arctic Code Vault. As such, it also includes, as an appendix, visual copies of the Guide to the GitHub Code Vault, along with an index of the archive&#39;s fifteen thousand most significant code repositories, including brief descriptions and locations within the archive.

It is perhaps worth noting that our advisory board stressed that ours is likely to be the best-documented era in human history by far, so bundling the Tech Tree with the archive is likely to be more convenient than essential for its inheritors. As such, it is entirely possible -- indeed quite likely -- that its value will consist largely of providing context regarding the era and culture in which the archive was created, rather than as a source of new and unavailable knowledge, though of course there are imaginable futures in which it plays the latter role.

What follows is a brief summary of each section, describing both the general topics it covers, and the works the Tech Tree includes to document our current understanding of those topics.

## Fundamentals of computing and the Internet

These books describe what computers are, from the silicon up -- electricity, transistors, binary logic, digital gates, bits, bytes, chips, ALUs, microprocessors, software -- as well as introducing what they can do. It also includes books which describe, at a high level, how computers can be connected together, and what that means. The works in question are:

_The Pattern On The Stone_ by W. Daniel Hills (Basic Books)

_But How Do It Know?_ by J. Clark Scott (John C Scott)

_Code: The Hidden Language of Computer Hardware and Software_ by Charles Petzold (Pearson Education)

_Computer Fundamentals_ by Anita Goel (Pearson Education)

_How The Internet Really Works_ by Ulrike Uhlig, Mallory Knodel, Niels ten Oever, Corinne Cath, and Catnip (No Starch)

## Algorithms and data structures

These are the fundamentals of computer science, and hence the foundation of software engineering; describing how data is structured and stored, and the most effective and efficient ways in which it can be processed.

_The Art of Computer Programming_ by Donald Knuth (Pearson)

_Algorithmic Thinking_ by  Daniel Zingaro (No Starch)

_Sequential and Parallel Algorithms and Data Structures_ by Peter Sanders, Kurt Mehlhorn, Martin Dietzfelbinger, Roman Dementiev (Springer)

_Cryptography_ by Simon Rubinstein-Salzedo (Springer)

_Mastering SciPy_ by Francisco J. Blanco-Silva (Packt)

_Everyday Data Structures_ by William Smith (Packt)

_Database Internals_ by Alex Petrov (O&#39;Reilly)

_Introduction to the Theory of Computation_ by Michael Sipser (Cengage)

_Think Like A Programmer_ by V. Anton Spraul (No Starch)

_Write Great Code_ by Randall Hyde (No Starch)

## Compilers, assembler, and operating systems

The purpose of the Archive Program is to preserve software, and these are the fundamental building blocks of software. These books help to explain how high-level written software becomes low-level electrical impulses:

_A Practical Approach To Compiler Construction_ by Des Watson (Springer)

_The Secret Life Of Programs_ by Jonathan Steinhart (No Starch)

_The Art of Assembly Language_ by Randall Hyde (No Starch)

_Understanding the Linux Kernel_ by Daniel P. Bovet and Marco Cesati (O&#39;Reilly)

_Mastering Linux Kernel Development_ by Raghu Bharadwaj (Packt)

_The Linux Programming Interface_ by Michael Kerrick (No Starch)

## Programming languages

There are hundreds of programming languages; the enormous chart visualizing their evolution at the Computer History Museum is worth visiting if you&#39;re a developer, and we don&#39;t intend to document them all. Still, accessible book-length descriptions of a selection of the world&#39;s major languages seems desirable.

_Introducing Python_ by Bill Lubanovic (O&#39;Reilly)

_Comprehensive Ruby Programming_ by Jordan Hudgens (Packt)

_LISP, Lore, and Logic_ by W. Richard Stark (Springer)

_The C Programming Language_ by Kernighan and Ritchie (Pearson)

_Learn C The Hard Way_ by Zed Shaw (Pearson)

_Head First C_ by David Griffiths, Dawn Griffiths (O&#39;Reilly)

_Effective C_ by Robert Seacord (No Starch)

_The C++ Primer_ by Stanley B. Lippman, Josée Lajoie, and Barbara E. Moo (Pearson)

_Programming Rust_ by Jim Blandy and Jason Orendorff (O&#39;Reilly)

_The Rust Programming Language_ by Steve Klabnik and Carol Nichols (No Starch Press)

_The Go Programming Language_ by Alan A. A. Donovan and Brian W. Kernighan (Pearson)

_Head First Go_ by Jay McGavren (O&#39;Reilly)

_Learning Java_ by Patrick Niemeyer and Daniel Leuck (O&#39;Reilly)

_The Java Virtual Machine Specification_ by Tim Lindholm, Frank Yellin, Gilad Bracha, and Alex Buckley (Pearson)

_JavaScript: The Definitive Guide_ by David Flanagan (O&#39;Reilly)

_JavaScript: The Good Parts_ by Douglas Crockford (O&#39;Reilly)

_Automate the Boring Stuff with Python_ by Al Sweigart (No Starch)

_Learning Swift_ by Jonathon Manning, Paris Buttfield-Addison, and Tim Nugent (O&#39;Reilly)

_Introducing Erlang_ by Simon St. Laurent (O&#39;Reilly)

_Clojure Programming_ by Chas Emerick, Brian Carper, and Christophe Grand (O&#39;Reilly)

_Clojure for the Brave and True_ by Daniel Higginbotham (No Starch)

_The Art of R Programming_ by Norman Matloff (No Starch)

_Mastering Scientific Computing with R_ by Paul Gerrard and Radia M. Johnson (Packt)

_Learn You A Haskell For Great Good_ by Miran Lipovaca (No Starch)

## Networking and connectivity

Computers are great, but in a way, so 20th century; it&#39;s _networked_ computers which are, at least arguably, the real technical revolution of the 21st. As such our networking protocols and technologies deserve considerable attention. We might hope our inheritors will either have long surpassed our networking, or will have the freedom to design anew rather than be shackled by all the compromises we&#39;ve needed to make for the sake of backwards compatibility but either way, hopefully they can learn something from what we&#39;ve done. Which is described by:

_Cabling: The Complete Guide To Copper and Fiber-Optic Networking_ by Andrew Oliviero and Bill Woodward (Wiley)

_Ethernet: The Definitive Guide_ by Charles E. Spurgeon and Joann Zimmerman (O&#39;Reilly)

_Understanding TCP/IP_ by Alena Kabelová and Libor Dostálek (Packt)

_TCP/IP Essentials_ by Shivendra S. Panwar, Shiwen Mao, Jeong-dong Ryoo, and Yihan Li (Cambridge)

_DNS and BIND_ by Cricket Liu and Paul Albitz (O&#39;Reilly)

_BGP_ by Iljitsch van Beijnum (O&#39;Reilly)

_HTTP: The Definitive Guide_ by David Gourley, Brian Totty, Marjorie Sayer, Anshu Aggarwal, and Sailu Reddy (O&#39;Reilly)

_Implementing SSL / TLS Using Cryptography and PKI_ by Joshua Davies (Wiley)

_Nginx HTTP Server_ by Martin Fjordvald and Clement Nedelcu (Packt)

_sendmail_ by Bryan Costales, Claus Assmann, George Jansen, and Gregory Neil Shapiro (O&#39;Reilly)

_Programming Internet Email_ by David Wood (O&#39;Reilly)

_Data Communications and Networking_ by Behrouz A. Forouzan (McGraw-Hill)

_Computer Networking: Principles, Protocols, and Practice_ by Olivier Bonaventure (Pearson)

_Computer Networking: A Top-down Approach_ by Jim Kurose (Pearson)

## Modern software development

The line-by-line act of writing software is quite different from the team-by-team process of developing, testing, integrating, and deploying it. A few key approaches, tools, and roles are described here, including, for obvious reasons, unpacking Git itself.

_Working in Public: The Making and Maintenance of Open Source Software_ by Nadia Eghbal (Stripe Press) /

_The Manager&#39;s Path_ by Camille Fournier (O&#39;Reilly)

_The Missing README_ by Chris Riccomini and Dmitriy Ryaboy (No Starch)

_Learning Agile_ by Andrew Stellman and Jennifer Greene (O&#39;Reilly)

_Professional Git_ by Brent Laster (Wiley)

_Tangled Web: A Guide to Securing Modern Web Applications_ by Michal Zalewski (No Starch)

_Metasploit_ by David Kennedy, Jim O'Gorman, Devon Kearns, and Mati Aharoni (No Starch)

_Effective DevOps_ by Jennifer Davis and Ryn Daniels (O&#39;Reilly)

_Site Reliability Engineering_ edited by Betsy Beyer, Chris Jone, Jennifer Petoff &amp; Niall Richard Murphy (O&#39;Reilly)

_Designing Distributed Systems_ by Brendan Burns (O&#39;Reilly)

_Designing Data-Intensive Applications_ by Martin Kleppmann (O&#39;Reilly)

_Exercises in Programming Style_ by Cristina Videira Lopes (CRC Press)

## Modern software applications

It would take a tech forest, not a tree, to even try to describe all of the uses to which software is put. However, some depictions of how individual projects and libraries are knit together into powerful networked applications seem valuable, as do overviews of e.g. virtualization, &quot;big data&quot; software, and especially machine learning.

### Web development

_Web Development with Node and Express_ by Ethan Brown (O&#39;Reilly)

_Flask Web Development_ by Miguel Grinberg (O&#39;Reilly)

_RESTful Web APIs_ by Leonard Richardson, Mike Amundsen, Sam Ruby (O&#39;Reilly)

_Ruby on Rails Tutorial_ by Michael Hartl (Pearson)

_Django for Professionals: Production Websites with Python & Django_ by William S. Vincent (Still River)

### Machine learning

_Deep Learning from Scratch_ by Seth Weidman (O&#39;Reilly)

_Deep Learning: A Visual Approach_ by  Andrew Glassner

_Fundamentals of Deep Learning_ by Nikhil Buduma and Nicholas Locascio (O&#39;Reilly)

_Practical Convolutional Neural Networks_ by Mohit Sewak, Md. Rezaul Karim, and Pradeep Pujari (Packt)

_Pattern Recognition and Machine Learning_ by Christopher Bishop (Springer)

_Generative Deep Learning_ by David Foster (O&#39;Reilly)

_Strengthening Deep Neural Networks_ by Katy Warr (O&#39;Reilly)

### Virtualization and containers

_Mastering Docker_ by Scott Gallagher (Packt)

_Kubernetes: Up and Running_ by Brendan Burns, Joe Beda, and Kelsey Hightower (O&#39;Reilly)

_Spark: The Definitive Guide_ by Bill Chambers, Matei Zaharia (O&#39;Reilly)

### Reliability and scaling

_Database Reliability Engineering_ by Laine Campbell and Charity Majors (O&#39;Reilly)

_The Art of Capacity Planning_ by Arun Kejariwal and John Allspaw (O&#39;Reilly)

### Economics and sociotechnical systems

_The Economics of Information Technology_ by Hal Varian, Joseph Farrell and Carl Shapiro (Cambridge University Press)

_Mastering Bitcoin_ by Andreas Antonopoulos

## Hardware architectures

The spectrum of complexity from a single analog transistor to a modern multicore processor is, needless to say, difficult to summarize. This section tries to describe the basics of digital circuits and microprocessors, along with a few key references, before going on to hardware architectures and hardware design languages.

### Modern hardware architecture

_Microprocessor Design_ by Grant McFarland (McGraw-Hill)

_Microprocessor Architecture_ by Jean-Loup Baer (Cambridge)

_Inside the Machine_ by Jon Stokes

_Introduction to Parallel Processing_ by Behrooz Parhami (Springer)

### HDLs

_IEEE Standard VHDL Language Reference Manual_ (IEEE)

_IEEE Standard for SystemVerilog_ (IEEE)

### Example architecture details

_Arduino: A Technical Reference_ by J. M. Hughes (O&#39;Reilly)

_RISC-V Specifications_ by the RISC-V International Technical Committee

_Learning FPGAs_ by Justin Rajewski (O&#39;Reilly)

## Hardware development

_Digital Computer Electronics_ by Albert P. Malvino and Jerald A Brown (Career Education)

_Computer Time Travel_ by JS Walker (Oldfangled)

_Theory, Design, and Applications of Unmanned Aerial Vehicles_ by A.R. Jha (CRC Press)

_Modern Robotics_ by Kevin Lynch and Frank Park (Cambridge University Press)

_Mastering ROS for Robotics Programming_ by Lentin Joseph (Packt)

## Electronic components, transistors, semiconductor manufacturing

A more low-level analysis of fundamental electronic components and transistor-based circuitry, along with textbooks describing lithography and chip manufacturing. Obviously such manufacturing is essentially impossible to recreate from scratch (Moore&#39;s lesser-known second law described how fabricator costs increase just as chip density decreases) but these works could conceivably be of historical or even practical significance.

_Fundamentals of Semiconductor Manufacturing_ by Gary S. May and Simon M. Sze (Wiley)

_Semiconductor Manufacturing Handbook_ (both editions) by Hwaiyu Geng (McGraw-Hill)

## Pre-industrial technologies

These are the works which address the &quot;romantic catastrophe&quot; image of the archive&#39;s inheritors, who seek to reboot all of modern technological civilization from pre-industrial scratch. Such possible futures do exist, although they seem unlikely; furthermore, it seems possible that these works might help fill in gaps which arise in historical knowledge.

_The Knowledge_ by Lewis Dartnell (Penguin)

_Caveman Chemistry_ by Kevin Dunn (Universal)

_Practical Blacksmithing_ by M.T. Richardson (Weathervane)

_Materials Handbook_ by George S. Brady Henry R. Clauser, and John A. Vaccari (McGraw-Hill)

_Practical Self-Sufficiency_ by Dick and James Strawbridge (DK)

_Oxford Handbook of Infectious Diseases and Microbiology_ by Estée Török, Ed Moran, and Fiona Cooke (OUP)

## Fiction, culture, and history

It is our belief that culture is often best expressed through great works of fiction. As such, we sought to assemble a list of notable literary works (including / beginning with a few books of nonfiction) to convey, on a human level, the history and culture of our time. These are:

_Chapman&#39;s Homer_

_The Complete Works of William Shakespeare_

_The Tale of Genji_ by Murasaki Shikibu

_Crime and Punishment_ by Fyodor Dostoevsky

_Extraordinary Popular Delusions and the Madness Of Crowds_ by Charles Mackay

_I, Claudius_ by Robert Graves

_Brave New World_ by Aldous Huxley (Harper Perennial)

_1984_ by George Orwell (Signet Classics)

_Cyberiad_ by Stanislaw Lem (Mariner)

_One Hundred Years Of Solitude_ by Gabriel García Márquez (Harper Perennial)

_Foucault&#39;s Pendulum_ by Umberto Eco (Mariner)

_Anathem_ by Neal Stephenson (William Morrow)

_Magic for Beginners_ by Kelly Link

## Cultural context

This section of the Tech Tree is intended to convey both useful practical information from our culture, and a depiction of what it was like at the time the archive was written. It will consist of encoded data, rather than imaged pages, largely because its centerpiece, a snapshot of Wikipedia, is far too large for the latter format.

Wikipedia, while not without its flaws and omissions, is the most readily available proxy for &quot;a written summary of our world.&quot; Note that this section is by no means intended as a complete depiction of humanity today: as our advisors stressed, this era is likely to be the best documented in all of human history, and such information is very unlikely to be difficult to find. Rather, it is intended as a convenience to indicate to the archive&#39;s inheritors the specific, particular context of the era in which the archive was written.

This section will also include several other data sources recommended by GitHub&#39;s community:

- Wiktionary
- Wikispecies
- The File Formats Archive

## The GitHub Arctic Code Vault

As the Tech Tree is a companion piece to the GitHub Arctic Code Vault, it will contain an index with the name, brief description, and film reel number for all of the GitHub repositories stored in the Arctic Code Vault, i.e. every active public GitHub repo as of 02/02/2020.

This index will also highlight the 15,000 GitHub repositories which are the most-starred or most-depended-on at the time the archive was written. (These are also the repositories which will be stored in the two-reel &quot;greatest hits&quot; subsets of the archive, to be kept with partners such as Oxford&#39;s Bodleian Library and others.)

It is worth noting that every individual reel of the Arctic Code Vault also has its own index itemizing its contents, along with all of the instructions and information required to decode the information stored in that reel. This master index will be a superset of all of those indexes, to serve as a backup and a convenience for the archive&#39;s inheritors.

