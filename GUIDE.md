# A Guide To the GitHub Code Vault

## Introduction

This archive, the GitHub Code Vault, was established and preserved by the GitHub Archive Program, whose mission is to preserve open source software for future generations. You may be reading this one year from now, or one thousand, but either way, we hope its contents, and perhaps the very concept of open source, are useful to you.

This is primarily an archive of software. Software is a series of commands used to control the actions of a computer. A computer is a device which can automatically perform mathematical functions so much faster than a human mind that it has powers far beyond us. Our computers are used to help explore the secrets of the universe, to connect all of humanity in an omnipresent web of information, to manipulate signals fast enough to transmit sounds and project detailed moving images onto electrical screens, and to control enormously powerful machinery which far exceeds both the capacity and precision of human labor.

A computer without software can do none of these things. A computer is an extraordinary and marvelous thing, but without software, all its power is useless. The purpose of this archive is to pass what we know about software on to you.

Open source software is not a different kind of software, but a different ethos. Software is written as complex but human-readable sequences of commands, the various flavors of which are known as programming languages, because a complete unit of software is often called a program. These programs are then converted into the binary language of ones and zeros used by computers. This process is known as compiling.

Because compiled software is very difficult to decipher back into its original program form, also known as its source code, it is possible for people to keep that original form secret and claim ownership over it. The open source ethos rejects that kind of secrecy and ownership. Open source software is made available to any and all who want to use it, at no cost, so they can in turn improve it, or use it to build something new and better.

An open source software project is the collective work of a self-organizing community which may number in the thousands. The accumulation of all open source projects archived here is the work of a community of many millions. While certain individuals may have special rights within any given project, such as the ability to approve or reject suggested changes to the latest official version of its source code, no one ever owns it. Every person has every right to take and use a complete copy of any open source project at any time, at no cost or penalty. This is known as forking a project.

When many people work on source code at the same time, it is difficult to keep track of and integrate all of their changes. An open source project known as Git is devoted to solving this problem. It integrates a complete history of all additions and changes to a project into an entity known as a git repository. This archive is essentially an archive of such repositories.

What follows is a description of what we believe you will need to know and have in order to make best use of this software archive. If you do not know or understand some or any of this, do not despair! We have also included a guide to how to accomplish these requirements. If for any reason you cannot accomplish them yourselves, then your descendants can.

## What You Need To Use The Archive

In principle, all you need to access the contents of this archive is a light source and some kind of magnifier. However, most (though not all) of its data has been packed very tightly onto these 200 film reels in an encoded and compressed form. Reading, decoding, and uncompressing this data will require considerable computation itself. In theory it could be done without computers, but it would be very tedious and difficult.

Our expectation is that you didn't need the definitions of software, computer, and other terms. We imagine you have computers of your own, probably vastly more advanced than ours, and possibly fundamentally differently architected. Once you understand the overview and guide below you will easily be able to access all of the data.

However, it's possible that you have inferior computers to ours, or even no computers at all. In case of that eventuality, we have prepared an uncompressed, unencoded, human-readable reel of data which we call the Tech Tree. The Tech Tree contains information about our fundamental technologies, our computers, and our software, in the hopes that, over time, you will be able to use this knowledge to recreate computers that can make use of the open source software in this archive.

## What's Inside

The archive is so large -- roughly 24 trillion bytes -- because it is extremely inclusive and democratic. Many millions of people make the software they write available to everyone. This archive includes a snapshot -- that is, a single copy, at a single moment in time -- of all the public software that GitHub's users are actively developing. This means it includes tens of millions of separate repositories. Our hope is that this wide, democratic approach will be of interest to historians of the future.

Of course, not all of these are equally important in terms of their influence and dependencies. The Tech Tree includes an index and brief description of the most significant repositories in the archive, and lists which reel each can be found on, so that they can be accessed without having to wade through all these millions of repositories to determine which are most practically useful.

## An Overview Of The Archive

The archive consists of 201 reels of film: one 'guide reel' of human-readable information and guidance, and 200 reels of archived software. Each reel includes 65,000 individual frames. The frames at the beginning of each reel, and the frames of the guide reel, include human-readable text and images. All other frames of film consist of digital data stored as QR codes.

Digital data means data ultimately stored in binary format, i.e. as 0s and 1s, because computers themselves are binary -- controlled by electrical signals which are either 'on' or 'off', corresponding to 1 or 0 -- and so binary data is vastly easier for computers to understand than any other.

The human-readable metadata stored at the beginning of each reel includes information about the film itself, a guide to the QR encoding used, a software program to decode it, and an index. The index lists the title, beginning frame number, and checksum for each file stored on that reel.

A file is a single coherent data entity. A checksum is a unique value from a calculation, known as a hash function, run over the entire contents of a file, to ensure that its contents have not been damaged or corrupted; the hash function used in the archive is known as SHA-1.

Each QR code consists of a field of tiny white or black squares which occupy almost the entire frame of film. We use QR codes because they are much more compact and robust than human-readable text. A QR code decodes into binary data, i.e. a series of ones and zeros.

This decoding is only the first step in turning that binary data into meaningful information. It is compressed data, meaning that it has been compacted to save space, similar to how one might write '128xA' rather than writing the letter 'A' 128 times. After being decoded, it must be decompressed.

The result after decompression is known as an archive file: a single file containing the entire contents of a single software project's repository. Most repositories include many files, so this archive file is like a book which contains many separate chapters, or a box which contains many other boxes. It is generally advantageous, though not absolutely necessary, to unpack the archive file into its component files before accessing them.

Finally, each component file is its own set of binary data, that is, ones and zeros. One can make sense of data if you know its format. For instance, in the format known as "UTF-8," the most common format in the archive, the ones and zeroes are divided into groups of eight, known as bytes, the byte 01000001 represents the letter A;  the three bytes 01101001 01101110 01110100 represent the word int; and the two bytes 11000011 10000011 represent the letter Ã (A with a tilde accent on top.)

This data archival process, binary files packed into archive files which have been first compressed and then QR-encoded, is obviously complex compared to simply writing human-readable text. The unarchiving process you will need to go through -- QR to compressed binary; compressed to uncompressed; archive file to multiple files; text files to human-readable text -- is similarly complex. That is because this complexity allows us to store vastly more data than would otherwise be possible, in a relatively easily computer-readable way.

If this complexity is difficult and costly for you, we apologize, but our expectation is that, if this is the case, this guide and the human-readable Tech Tree, will alleviate this complexity, and may perhaps be more useful to you than the archive contents, at least until your computers are advanced enough that the complexity of the archive's data is easy to deal with.

## Files, Directories, Repositories, and Data Formats

It may be instructive to discuss how the archive is logically divided. In particular, a discussion of files, directories, and data formats is likely to be helpful.

A file is a collection of data grouped together into a coherent entity with a single name: think of data as sand, and a file as a kind of bag which can hold sand, and only sand. A directory is a collection of files: think of it as a kind of bag which can only hold other bags. Following this metaphor, every repository consists of an outer directory, known as the root directory, which contains a number of files and/or a number of directories. Each directory can, in turn, contain both files and directories itself.

This structure is preferred because files organized into groups are much easier to work with than a single collection of files. The identifier of a particular file within the outer directory consists of the names of all of its enclosing directories, starting with the root, followed by its own individual name, with a / character between every name. For instance, a file named README.md in the root directory would be identified as /README.md and a file identified as /public/www/index.html would be the file index.html in the 'www' directory inside the 'public' directory inside the root directory.

Each repository in turn has two names, separated by a divider, which in the archive is an _ or underscore character. (Historically it has been a / or slash, but that is also used to indicate a directory, so we use _ for clarity.) The first name is the GitHub account which owns that repository; the second is the name of the individual repository. The combination of repository and file identifiers can be used to uniquely identify an individual file in the archive. For instance, the file 'package.json' in the directory 'web' in the repository 'ykarma' owned by the GitHub user 'rezendi' could be uniquely identified as /web/package.json in rezendi_ykarma in the archive.

Different kinds of files have different purposes. The GitHub archive consists largely of text files, meaning files whose data is meant to represent written language. Most software is written in text files containing highly structured text known as source code. A special program known as a compiler converts that human-readable source code into computer-readable instructions known as compiled code or machine code.

Files which are not text files, such as files which represent visual images or contain compiled code, are often referred to as binary files. This is unfortunately a misleading term, as text files are ultimately 1s and 0s as well. We will refer to files which are not text files as non-text files.

There are many ways to represent written human language using 1s and 0s. For historical reasons, most source code was originally written in what is known as Latin script. Latin script has 26 basic characters which are used to represent speakable words, each of which has two forms, upper case and lower case. It also has 10 digits to represent numbers. Latin script, along with various other associated symbols used to indicate structure and other concepts, is encoded into 1s and 0s in a format known as ASCII, which can represent 128 different characters and for historical reasons was dominant across most software for many years.

However, Latin script is only a tiny subset of the many ways in which humans express themselves in written language. To support other scripts, while also allowing all the software which had been written to use ASCII to continue working without changes (a concept known as backwards compatibility), another data format known as UTF-8 was introduced.

ASCII remains the most common format of source code. Every reel of this archive includes a guide to ASCII characters. ASCII is a subset of UTF-8, which is to say, all ASCII encodings are UTF-8 encodings as well. The guide reel additionally contains a specification of all UTF-8 characters. Almost all text files in this archive should be encoded as UTF-8.

Non-text files include files meant to represent images and formatted documents. A widely used convention is for a file to end with a . character followed by a suffix which indicates its type. For instance, a file which ends with .jpg is likely a JPEG image file; one which ends with .PNG is likely a Portable Network Graphic image file; and one which ends with .pdf a Portable Document File formatted document.

There is no single suffix which indicates text files. Rather, for source code, the suffix is more likely to indicate which programming or markup language the code is written in. Programming and markup languages will be described in more detail below.

## How To Extract The Archive's Contents

Here we will provide an overview of how to unpack a particular archived repository into its various constituent files. Again, this process consists of:

1.  Identifying the specific reel and frames on which the repository's data is archived.

2.  Decoding from the QR codes, the fields of black, white, and gray pixels on those frames, into a binary file, a sequence of (at least thousands, and often millions of) 1s and 0s.

3.  Unzipping the binary file into a longer, uncompressed archive file.

4.  Unpacking the archive file into the separate subfiles it contains. Note however that archive data is generally comprehensible, although messy, even if this step is omitted.

5.  Finally, converting each of those subfiles -- themselves sequences of 1s and 0s which may range from quite short to very long -- into written characters, if they are text files.

### Identifying the specific reel and frames on which the repository's data is archived

Each reel of film begins with a leader of empty film, and then the Zero Reference Frame, which consists of a solid black rectangle in one corner of an otherwise empty frame. The next human-readable frame is the Control Frame, with information about the reel. Following that is the Table Of Contents, which in turn includes a list of User Data Files.

Each repository on this reel is one of those User Data Files. The list includes a unique ID, a reel ID and a name for each of those files. For instance, the CPython repository might have the reel ID listed as 12345 and the name listed as python_cpython.tar.

Following the list of User Data Files is a list of Digital Data Locations. This list includes an ID, a start frame, a start byte, an end frame, and an end byte. So, using the hypothetical CPython example, the item in this list with the ID 12345 might have a start frame of 054321, a start byte of 03210321, an end frame of of 054545, and an end byte of 12321232.

This means, to get the CPython data: Go to frame 54321 of this reel of film. Decode all frames from the start frame, 54321, to the end frame, 54544, into binary values, by the means described below. This will give you 224 pieces of data numbered from 54321 to 54544, which will begin with a set of blank pieces with no data. Discard the first 3210320 bytes in the first non-blank piece of data. Append all the  "middle" pieces of data, in order. Finally, append the first 12321232 bytes from the last piece of data, 54544. You have now assembled the complete CPython repository, as a single compressed archive file.

### Decoding from the QR codes into a binary file

The details of how to decode the film frames into binary data are found in the human-readable Representation Information which is found following the Table of Contents at the beginning of every reel of film on the archive. This information is found on every reel so that, even if an individual reel is separated from the archive, it will still be possible to decipher its contents. That Representation Information includes, in order:

1.  A Guide to the GitHub Archive Program (this document)

2.  GitHub descriptive index, a list and brief description of all the repositories on this reel

3.  Representation Information description

4.  Digital Preservation and How to Retrieve Data, an overview of data retrieval details

5.  Storage Medium description

6.  Data Retrieval Technology

7.  Generic Preservation Reel Structure (reel format)

8.  Generic 4K Frame format description

9.  Unboxing library description

10. Unboxing library source code

11. ASCII data format specification

12. C programming language specification

13. LZMA / XZ source code

14. TAR archive file source code

15. PDF source code

16. [Rosetta Document?]

The sixth of those items, the Data Retrieval Technology document, describes the requirements and processes to use a scanner to capture the data on a single digitally encoded frame of film and turn it into a form amenable to computer analysis. The eighth of them, the Generic 4K Frame format description, provides the technical information, including source code, required for a computer to take such a scanned image and convert it into binary data.

It is theoretically possible, in principle, to convert a repository from QR-encoded data to binary data without using a computer. However, it would be enormously difficult and would probably require a sizable effort from a well-organized community over many weeks, if not months or years. Since the contents of the repositories are software intended to run on a computer, their use in the absence of a computer would be minimal at best.

In the event that the inheritors of this archive do not have computers, they should keep the archive whole and safe until they do. One purpose of the human-readable Tech Tree is to help accelerate the development of technologies and computers in case of this eventuality. (Its other purpose is to codify our technology and its development for future historians.)

### Unzipping the binary file into a longer, uncompressed archive file

In order to include as many repositories and as much data as possible, the data has been compressed. Compression means using a small amount of data to represent a larger amount, by use patterns and repetition in that larger amount. For instance, instead of writing the  character a nine times in a row, one could just write the compressed text 9a, if one was confident the reader would understand that 9a meant the uncompressed text aaaaaaaaa.

Effective compression algorithms are much more complex than that, but the same principle applies. This archive uses an algorithm known as LZMA, the human-readable source code for which is included in the Representation Information at the beginning of every reel.

LZMA combines what are known as an LZ77 algorithm and range encoding. LZ77 replaces repeated data with references to previous appearances of that data. For instance, to grossly oversimplify, if a 80-byte phrase appears twice, 400 bytes apart, the second time, the algorithm essentially compacts the data by saying "repeat 80 bytes from 400 bytes ago." Range encoding essentially converts an entire message into a single very long number, which in turn can be encoded.

The specific steps of the algorithm to be used to decompress the data are described by the LZMA source code contained in the Representation Information. While it's theoretically possible to decompress by hand, again, this would be an extremely time-intensive and labor-intensive process. In practice, a working computer would be called for.

### Unpacking the archive file into the separate subfiles it contains

At this point you have a single file known as a TAR file, for Tape Archive. A TAR file is essentially composed by grouping a number of files together by connecting the end of one to the beginning of the next, like taping individual pieces of paper together into a single scroll. A TAR file can include any number of files, of any size, divided into any number of directories and subdirectories.

Each subfile within a TAR file is prefaced by a 512-byte header record, which acts like the tape in the scroll metaphor. This header record contains information about the file, such as its name and size. The end of the archive is indicated by at least two consecutive 512-byte blocks.

Every repository archive file in this archive should begin with a single metadata file, which includes information about the repository, followed in turn by every file in the repository. This metadata file contains: [specify the repository metadata added to each tar file].

Because TAR files are essentially just collections of files with text records between them, if a TAR file contains all text files, it can be treated as a text file itself. If it contains a mixture, it can be treated as a text file which contains a mixture of structured, meaningful text  (the constituent text files) and incomprehensible gibberish (the constituent non-text files.)

Specific details of TAR files, and the software to encode and decode them, can be found in the Representation Information in every reel of the archive.

### Converting each individual file into written characters

Humanity has used many written characters over the millennia. The encoding used to represent these characters as 1s and 0s within this archive is known as UTF-8. A single UTF-8 character, i.e. a single written symbol, can occupy anywhere from 1 to 4 bytes of binary data.

For historical reasons, because they were the most widely used in the time and region where and when software development began, a group of characters (and concepts) known as ASCII are most efficiently encoded, at 1 byte per character. Anything which is not ASCII is encoded as 2 or more bytes per character. Most of the text files in this archive are ASCII, but a substantial number are not. Many more will be mostly ASCII with occasional non-ASCII characters.

The detailed specifications of ASCII can be found in the Representation Information in every reel of the archive. [A 'Rosetta document,' containing the text of the Universal Declaration of Human Rights in almost every written language, can also be found in the Representation Information? It will definitely be in the archive, but currently uncertain whether it will be part of the Tech Tree or in the RI.] The detailed specifications of UTF-8 can be found in the guide reel.

## Kinds of Files

There are many different kinds of text files, created for different reasons. The primary kind here, the reason this archive exists, is source code. Source code is very dense, extremely structured text, in which symbols like { and ; have great importance.

The key thing about source code is that it is written to be read by compilers. Since compilers are software, another way of phrasing this is that source code is written to be read by computers. Good code is also written so that other humans, if they are skilled and educated in the field of software, can understand it; but it is only correct if a compiler can understand it.

That compiler will, in turn, through complicated sequences described in the Tech Tree, convert the source code into the sequences of ones and zeros that will cause the computer to perform the functions and activities described by the code. To take a very simple example, the line of code

_for (int i=0; i<5; i++) { }_

will be converted by the compiler into a series of binary instructions fed to the computer, which will cause a tiny part of the computer, called a register, to set its value to 0, and subsequently increment that value to 1, 2, 3, and then 4. (This is not intended as an example of useful code; it is just an illustration of the many-layered process of turning source code into running software.)

Other kinds of text files, such as JSON, XML, and HTML, are used to store data (as opposed to commands) for computers. They are generally also readable by humans, although their structured formats make them harder to read than less-structured storytelling text like this file.

Most other kinds of text files are intended to be eventually read by humans. Some are simple, mostly unstructured text, like this file you are currently reading. A kind you will encounter widely in the archive is Markdown, signified by the .md extension to a file, which is a kind of intermediate form meant to be readable by humans in their raw form and also, at the same time, structured so that computers can format them into more visually appealing and useful layouts. Most repositories in this archive have a README.md Markdown file, which is generally intended as an initial introduction to the repository, describing what it is, why it exists, and how to use it.

A brief overview of the most common forms of non-text files may also be useful. Compiled code is non-text. JPG and PNG files encode images in digital format, and MP3 and WAV encode audio. PDF files encode documents with precise, perfect formatting. And ZIP and TAR files, as previously mentioned, are container files which may in turn include one more many other files.

## Human Languages and Programming Languages

### Human Languages

There are thousands of written languages used by humanity today, and even more spoken languages. Most of those are used only by relatively small populations, but there are at least twenty languages used as a first or second language by at least 60 million people.

The most widely used languages in the world are English and Chinese. For historical reasons, for many years most software development occurred in English-speaking nations, so for a time, English became the default language of software. Most programming languages use English words in their syntax. It is the language in which this guide to the archive was written.

It is not guaranteed that the inheritors of this archive will know English, although it does seem a particularly likely language to last indefinitely. In case some guidance to other languages is helpful, we are including the more than 500 available translations of the Universal Declaration of Human Rights [as an encoded, uncompressed UTF-8 file at the beginning of every reel?], and also in visual form within the Tech Tree. This declaration is a list of the rights and freedoms of every individual human being in our era, which may never be taken away.

### Programming Languages

Programming languages are those used by humans to communicate instructions to computers. They are the languages in which software is expressed. Other (trained) humans should also be able to read the software written in programming languages, but that is a secondary goal.

A programming language is a set of predefined elements, most of which are words, which can be arranged in a structured manner to instruct a computer to perform the specified action in the specified way. A collection of such instructions is known as a program, or as source code. Source code is essentially software in a frozen, written form.

Programs are generally divided into discrete steps, known as statements, which in turn are grouped together into collections known as functions. An entire program may be contained in a single file, or may be spread across thousands.

There are hundreds of different programming languages, spread across many different forms, approaches, and philosophies. Some are compiled into separate binary files, which are then executed; some, known as "interpreted" languages, are effectively compiled and run all at once, with no interim stage. Most modern languages include libraries of pre-written functions, and such libraries can be very voluminous and elaborate. Some of today's most popular programming languages include:

-   C, one of the oldest and fastest, most universal, and most powerful languages, simple in some ways but quite limited in others, and not always intuitive, easy to read, or easy to learn.

-   C++, a more complex, abstract, and powerful evolution of C.

-   C#, a further evolution compiled not into binary machine code but an interpreted 'runtime.'

-   Java, which is similar to (but predates) C#, is perhaps today's most widely used language.

-   JavaScript, quite unlike Java despite the similarity in name, and also known as ECMAScript, is a language initially used wholly within a web browser, i.e. a program which fetched, interpreted, and displayed data from a remote computer known as an Internet server; today, though, it is widely used on those servers as well.

-   TypeScript, a form of JavaScript with stricter rules so that errors, also known as bugs, are less likely to find their way into programs.

-   Python, an elegant language popular among scientists, both powerful and a good first language.

-   Ruby, an intuitive language whose statements often read almost like written English.

-   Go, a simple, powerful language which especially excels at parallelized programs, i.e. programs written such that multiple functions run independently at the same time.

-   Swift, a new language used to write for the phones and other devices used by a billion people.

-   Rust, intended as a replacement for C, one which makes dangerous bugs far less likely.

-   PHP, a clumsy but straightforward language used for Internet servers.

-   Lisp, a very old language with a fundamentally different, function-first approach to programming.

-   SQL, a very different kind of language used to fetch data from structured and highly efficient stores of data known as databases.

-   Assembler (or assembly), a very cryptic, limited, but fast and powerful family of languages wherein there is a direct relationship between the language constructs and the machine code of the computer in question; it may be considered half-compiled code.

## Development, Dependencies, and Open Source

### Development

The process of taking a single, simple source code file and converting it into electrical impulses within a computer is extremely complex. We deal with this complexity using layers of abstraction. An abstraction known as an instruction set allows the machine code output from a single compiler to be used on many different kinds of computers. An author of source code does not usually need to know or care what kind of computer, or even what instruction set, will be used to run that code; this is abstracted out by the compiler.

Modern software is, in turn, much more complex than a single author working on a single program for a single computer. It consists of many authors working on many files within a single project, simultaneously. Furthermore, every project depends on other, separate, self-contained projects as tools and/or components, while these projects are themselves actively being worked on, and are in turn dependent on yet other projects. Making all these moving parts work together elegantly and efficiently is the challenge of modern software development.

When multiple source code authors, also known as software developers, work on a single project, each has their own computer, and a copy of the entire project on their computer. If they each make changes, then each has a different version of the same project. The process of reconciling multiple versions of a project is known as version control. It is managed by version control software; in this archive, by software called git, after which GitHub itself is named. Every repository in this archive is a git repository.

Git can automatically merge different versions of software together into one coherent form with minimal human intervention required. Git also keeps a complete history which allows you to roll back to a previous version as and when needed. However, in order to save space, this archive's repositories generally do not include git histories.

When multiple developers take a project on multiple different paths simultaneously, this is known as branching a project, and those paths are known as branches. The agreed-upon main branch of a project is known as the trunk, or the master branch. Git provides a facility developers can use to summarize the differences between two branches and propose joining theirs into the other's. This is known as a pull request. Modern software development consists largely of branching a project, writing or editing the software on your branch, and, when finished, submitting a pull request for your work to be reincorporated back into the master branch.

### Dependencies

Essentially every programming language supports building upon the work of others. Without re-using others' work, every project would be enormously more difficult, and vastly slower, and vanishingly few projects would ever see actual use in the real world.

If project A needs to include project B in order for A to do its work, then A is known as dependent on project B, and B is known as a dependency of project A. A can have many dependencies, each of which can have many dependencies of their own, and so forth. Furthermore, each dependency is for a particular version, or range of versions, of a given project. The full itemization of all of a project's multiple layers of dependencies is known as its dependency tree.

Generally, dependencies are itemized inside source code files, usually at the very top, and each time the compiler or interpreter finds a dependency, it looks for it in a set of predefined directories. Because the dependency tree for a project can be very complex, it is sometimes itemized in its entirety in a single file within a project known as a package list. For instance, Ruby projects may have a Gemfile for this purpose, and JavaScript projects may have a package.json file. This allows a kind of tool known as package management software to fetch all the dependencies for a project at once, from one or more Internet servers.

In the case of this archive, it is likely that the dependencies for any given project exist elsewhere in the archive. [The archive is grouped by programming language to maximize the proximity of dependencies?] In order to find a dependency in the archive, one must first discover the correspondence between the name of the dependency in the source code or the package list; and second, use the master index in the guide reel, or, in its absence, the indexes at the front of each reel, to determine on which reel and frame(s) the repository in question can be found.

### Open source

Since running a program on a computer requires only the compiled machine code, it is possible to distribute that while keeping the source code secret. This is known as the closed source model, and, historically, was the early, crude approach to software development.

It has since been learned that making source code public, for anyone to copy, branch, and improve upon, is a far more effective approach to software development. More people who can read a project's source code means more people to identify possible needs and useful new features, more people who understand the project enough to contribute to it, more people who might spot bugs and submit fixes, and more people to test and verify that new code works.

In general, closed source leads to smaller, insular, fragmented communities who struggle to find and adopt new and better ideas. Open source leads to large, interconnected communities, each helping one another's projects grow and flourish and succeed, using each others' work as dependencies and/or reusing their code, and learning from one another. Open source software is a toolkit for the collective use of all humanity, and the more and better tools we have, the faster and better we can progress as a species.
