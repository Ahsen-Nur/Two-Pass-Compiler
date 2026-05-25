# TWO-PASS COMPILER 


# İçindekiler

1. [Proje Hakkında](#1-proje-hakkında)  
2. [Projenin Amacı](#2-projenin-amacı)  
3. [Compiler Nedir?](#3-compiler-nedir)  
4. [Compiler Mimarisi](#4-compiler-mimarisi)  
5. [Kullanılan Teknolojiler](#5-kullanılan-teknolojiler)  
6. [Proje Klasör Yapısı](#6-proje-klasör-yapısı)  
7. [Desteklenen Dil Özellikleri](#7-desteklenen-dil-özellikleri)  
8. [Compiler Çalışma Mantığı](#8-compiler-çalışma-mantığı)  
9. [Lexical Analysis (Lexer)](#9-lexical-analysis-lexer)  
10. [Syntax Analysis (Parser)](#10-syntax-analysis-parser)  
11. [Semantic Analysis](#11-semantic-analysis)  
12. [Abstract Syntax Tree (AST)](#12-abstract-syntax-tree-ast)  
13. [Symbol Table](#13-symbol-table)  
14. [Error Handling Sistemi](#14-error-handling-sistemi)  
15. [GUI Arayüzü](#15-gui-arayüzü)  
16. [Kurulum Adımları](#16-kurulum-adımları)  
17. [Projeyi Çalıştırma](#17-projeyi-çalıştırma)  
18. [Örnek Kod](#18-örnek-kod)  
19. [Projenin Teknik Detayları](#19-projenin-teknik-detayları)  
20. [Sonuç](#20-sonuç)

---

# 1. Proje Hakkında

Bu proje, System Programming dersi kapsamında geliştirilen iki geçişli (two-pass) basit bir compiler sistemidir.

Projede küçük ölçekli bir programlama dili tasarlanmış ve bu dil için:

- Lexer (Lexical Analyzer)
- Parser (Syntax Analyzer)
- Semantic Analyzer
- Abstract Syntax Tree (AST)
- Symbol Table
- GUI Tabanlı Compiler Arayüzü

tamamen sıfırdan geliştirilmiştir.

Projede herhangi bir hazır compiler-generator aracı kullanılmamıştır.

Özellikle aşağıdaki araçlar kullanılmamıştır:

- Lex
- Yacc
- ANTLR

Tüm compiler mantığı manuel olarak gerçekleştirilmiştir.

---

# 2. Projenin Amacı

Bu projenin temel amacı:

- Compiler çalışma mantığını anlamak
- Programlama dillerinin nasıl işlendiğini öğrenmek
- Lexical analysis mantığını kavramak
- Context-Free Grammar (CFG) yapısını anlamak
- Recursive Descent Parser geliştirmek
- Semantic analysis işlemlerini gerçekleştirmek
- AST üretmek
- Symbol table yönetimini öğrenmek

olarak belirlenmiştir.

---

# 3. Compiler Nedir?

Compiler, kaynak kodu analiz ederek onu başka bir forma dönüştüren yazılımdır.

Bu projede compiler aşağıdaki aşamalardan oluşmaktadır:

```text
Source Code
     ↓
Lexical Analysis
     ↓
Token Stream
     ↓
Syntax Analysis
     ↓
Abstract Syntax Tree
     ↓
Semantic Analysis
     ↓
Error Reporting
```

---

# 4. Compiler Mimarisi

Proje iki temel pass (geçiş) mantığıyla geliştirilmiştir.

## PASS 1 — Lexical Analysis

Kaynak kod karakter karakter okunur ve tokenlara ayrılır.

Örnek:

```c
int x = 10;
```

Token çıktısı:

```text
KEYWORD        int
IDENTIFIER     x
OPERATOR       =
INTEGER        10
DELIMITER      ;
```

---

## PASS 2 — Syntax & Semantic Analysis

Bu aşamada:

- Grammar kontrolü
- Operator precedence
- AST üretimi
- Variable kontrolü
- Type kontrolü
- Semantic error kontrolü

yapılır.

---

# 5. Kullanılan Teknolojiler

| Teknoloji | Amaç |
|---|---|
| Python | Compiler geliştirme |
| Tkinter | GUI geliştirme |
| Recursive Descent Parser | Syntax analysis |
| Object-Oriented Programming | AST ve compiler yapısı |
| Regex & String Processing | Tokenization |

---

# 6. Proje Klasör Yapısı

```text
compiler/
│
├── lexer/
│   ├── lexer.py
│   ├── token.py
│   └── token_types.py
│
├── parser/
│   ├── parser.py
│   └── ast_nodes.py
│
├── semantic/
│   └── semantic_analyzer.py
│
├── gui/
│   └── compiler_gui.py
│
├── tests/
│
├── main.py
│
└── README.md
```

---

# 7. Desteklenen Dil Özellikleri

Compiler aşağıdaki dil yapılarını desteklemektedir:

## Veri Tipleri

- int
- float

---

## Değişken Tanımlama

```c
int x;
float y;
```

---

## Assignment İşlemleri

```c
x = 10;
y = x + 5;
```

---

## Aritmetik Operatörler

```c
+
-
*
/
```

---

## Comparison Operatörleri

```c
==
!=
<
>
<=
>=
```

---

## Logical Operatörler

```c
&&
||
```

---

## if / else Yapısı

```c
if (x > 5) {

    print(x);

}
else {

    print(y);

}
```

---

## while Döngüsü

```c
while (x > 0) {

    x = x - 1;

}
```

---

## print Komutu

```c
print(x);
```

---


# 8. Compiler Çalışma Mantığı

Compiler aşağıdaki sırayla çalışmaktadır:

## 1. Source Code Okuma

Kullanıcının yazdığı kod alınır.

---

## 2. Tokenization

Kod tokenlara ayrılır.

---

## 3. Parsing

Grammar kontrol edilir.

---

## 4. AST Üretimi

Kodun ağaç yapısı oluşturulur.

---

## 5. Semantic Analysis

- Variable declaration kontrolü
- Type kontrolü
- Semantic error kontrolü

yapılır.

---

## 6. Sonuçların Gösterilmesi

GUI üzerinde:

- Tokens
- AST
- Symbol Table
- Errors

gösterilir.

---

# 9. Lexical Analysis (Lexer)

Lexer aşağıdaki işlemleri gerçekleştirmektedir:

- Source code okuma
- Token ayırma
- Keyword tanıma
- Identifier tanıma
- Number literal tanıma
- String literal tanıma
- Operator tanıma
- Delimiter tanıma
- Lexical error tespiti

---

## Desteklenen Token Türleri

| Token Türü | Açıklama |
|---|---|
| KEYWORD | Dil anahtar kelimeleri |
| IDENTIFIER | Değişken isimleri |
| INTEGER_LITERAL | Integer sayılar |
| FLOAT_LITERAL | Float sayılar |
| STRING_LITERAL | String değerler |
| OPERATOR | Operatörler |
| DELIMITER | Noktalama karakterleri |

---

# 10. Syntax Analysis (Parser)

Projede Recursive Descent Parser kullanılmıştır.

Her grammar kuralı için ayrı parser fonksiyonları yazılmıştır.

Örnek:

```bnf
assignment ->
IDENTIFIER "=" expression ";"
```

Parser fonksiyonu:

```python
parse_assignment()
```

---

# 11. Semantic Analysis

Semantic Analyzer aşağıdaki kontrolleri yapmaktadır:

## Variable Declaration Kontrolü

```c
x = 5;
```

Eğer x tanımlı değilse hata verir.

---

## Duplicate Variable Kontrolü

```c
int x;
int x;
```

Aynı variable tekrar tanımlanamaz.

---

## Type Checking

```c
int x;
x = "hello";
```

Type mismatch hatası oluşur.

---

# 12. Abstract Syntax Tree (AST)

Compiler parse işlemi sonucunda AST üretmektedir.

Örnek:

```c
x = y + 5;
```

AST:

```text
ASSIGNMENT
 ├── IDENTIFIER x
 └── OPERATOR +
      ├── IDENTIFIER y
      └── NUMBER 5
```

AST yapısı operator precedence mantığını korumaktadır.

---

# 13. Symbol Table

Compiler değişken bilgilerini Symbol Table içerisinde saklamaktadır.

Örnek:

| Variable | Type |
|---|---|
| x | int |
| y | float |

---

# 14. Error Handling Sistemi

Compiler üç farklı hata türünü desteklemektedir.

---

## Lexical Errors

Örnek:

```c
@
```

---

## Syntax Errors

Örnek:

```c
x = ;
```

---

## Semantic Errors

Örnek:

```c
x = 5;
```

x tanımlı değilse semantic error oluşur.

---

# 15. GUI Arayüzü

Compiler için Tkinter tabanlı GUI geliştirilmiştir.

GUI aşağıdaki bölümlerden oluşmaktadır:

- Source Code Editor
- Token Viewer
- AST Viewer
- Symbol Table Viewer
- Error Panel
- File Open
- File Save
- Compile Button

---

# 16. Kurulum Adımları

## 1. Repository İndir

```bash
git clone <repo_url>
```

---

## 2. Proje Klasörüne Gir

```bash
cd compiler
```

---

## 3. Virtual Environment Oluştur

```bash
python -m venv venv
```

---

## 4. Virtual Environment Aktifleştir

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

# 17. Projeyi Çalıştırma

```bash
python main.py
```

GUI açılacaktır.

---

# 18. Örnek Kod


```c
int x;
float y;

x = 10;

y = x + 5.5;

if (x > 5) {

    print(y);

}
else {

    print(x);

}

while (x > 0) {

    x = x - 1;

}
```

---


# 19. Projenin Teknik Detayları

Projede:

- Recursive Descent Parsing
- Context-Free Grammar
- Operator Precedence Parsing
- AST Construction
- Symbol Table Management
- Semantic Analysis

yaklaşımları kullanılmıştır.

---

# 20. Sonuç

Bu projede sıfırdan çalışan bir two-pass compiler sistemi geliştirilmiştir.

Compiler:

- Lexical Analysis
- Syntax Analysis
- Semantic Analysis
- AST üretimi
- Symbol Table yönetimi
- GUI tabanlı çıktı sistemi

özelliklerini başarıyla gerçekleştirmektedir.

Proje compiler mantığını anlamak açısından önemli bir deneyim sağlamıştır.

---