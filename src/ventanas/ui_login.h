/********************************************************************************
** Form generated from reading UI file 'loginczaRzk.ui'
**
** Created by: Qt User Interface Compiler version 6.5.2
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef LOGINCZARZK_H
#define LOGINCZARZK_H

#include <QtCore/QVariant>
#include <QtWidgets/QApplication>
#include <QtWidgets/QFrame>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_ContainerLogin
{
public:
    QFrame *LoginPrincipal;
    QLabel *logoSuperior;
    QLabel *fondoDegradado;
    QLabel *subContainerLogin;
    QLineEdit *cajaUsuarioLogin;
    QLabel *personasLogin;
    QLineEdit *cajaContrasennaLogin;
    QLabel *textoLogin;
    QLabel *iconoPersonaLogin;
    QPushButton *botonAceptarLogin;
    QLabel *esloganLogin;
    QLabel *separadorLogin;
    QPushButton *iconoFBLogin;
    QPushButton *iconoGoogleLogin;
    QPushButton *iconoTwitterLogin;
    QPushButton *iconoVolverAtrasLogin;
    QLabel *textoEnlaceRegistro;
    QPushButton *enlaceRegistrate;

    void setupUi(QWidget *ContainerLogin)
    {
        if (ContainerLogin->objectName().isEmpty())
            ContainerLogin->setObjectName("ContainerLogin");
        ContainerLogin->resize(704, 500);
        ContainerLogin->setStyleSheet(QString::fromUtf8(""));
        LoginPrincipal = new QFrame(ContainerLogin);
        LoginPrincipal->setObjectName("LoginPrincipal");
        LoginPrincipal->setGeometry(QRect(0, 0, 711, 501));
        LoginPrincipal->setStyleSheet(QString::fromUtf8("background-color: rgb(255, 255, 255);\n"
""));
        LoginPrincipal->setFrameShape(QFrame::StyledPanel);
        LoginPrincipal->setFrameShadow(QFrame::Raised);
        logoSuperior = new QLabel(LoginPrincipal);
        logoSuperior->setObjectName("logoSuperior");
        logoSuperior->setGeometry(QRect(20, 10, 51, 51));
        logoSuperior->setStyleSheet(QString::fromUtf8("border-image: url(:/images/logoUniConnect.png);"));
        fondoDegradado = new QLabel(LoginPrincipal);
        fondoDegradado->setObjectName("fondoDegradado");
        fondoDegradado->setGeometry(QRect(40, 90, 621, 391));
        fondoDegradado->setStyleSheet(QString::fromUtf8("border-image: url(:/images/FondoDegradado.png);\n"
""));
        subContainerLogin = new QLabel(LoginPrincipal);
        subContainerLogin->setObjectName("subContainerLogin");
        subContainerLogin->setGeometry(QRect(400, 130, 201, 331));
        QFont font;
        font.setStyleStrategy(QFont::PreferDefault);
        subContainerLogin->setFont(font);
        subContainerLogin->setStyleSheet(QString::fromUtf8("\n"
"background-color: rgb(252, 252, 252);\n"
""));
        subContainerLogin->setFrameShape(QFrame::NoFrame);
        cajaUsuarioLogin = new QLineEdit(LoginPrincipal);
        cajaUsuarioLogin->setObjectName("cajaUsuarioLogin");
        cajaUsuarioLogin->setGeometry(QRect(430, 260, 141, 21));
        cajaUsuarioLogin->setStyleSheet(QString::fromUtf8("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;"));
        personasLogin = new QLabel(LoginPrincipal);
        personasLogin->setObjectName("personasLogin");
        personasLogin->setGeometry(QRect(100, 140, 261, 221));
        personasLogin->setStyleSheet(QString::fromUtf8("border-image: url(:/images/logoSinFondo.png);\n"
"background-color: transparent;\n"
""));
        cajaContrasennaLogin = new QLineEdit(LoginPrincipal);
        cajaContrasennaLogin->setObjectName("cajaContrasennaLogin");
        cajaContrasennaLogin->setGeometry(QRect(430, 310, 141, 21));
        cajaContrasennaLogin->setAcceptDrops(true);
        cajaContrasennaLogin->setStyleSheet(QString::fromUtf8("background-color: rgba(0,0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(55, 158, 210);\n"
"color:rgba(0,0,0,240);\n"
"padding-bottom:7px;"));
        textoLogin = new QLabel(LoginPrincipal);
        textoLogin->setObjectName("textoLogin");
        textoLogin->setGeometry(QRect(430, 210, 151, 31));
        QFont font1;
        font1.setPointSize(15);
        font1.setBold(true);
        textoLogin->setFont(font1);
        textoLogin->setStyleSheet(QString::fromUtf8("border-color: rgb(52, 136, 196);"));
        iconoPersonaLogin = new QLabel(LoginPrincipal);
        iconoPersonaLogin->setObjectName("iconoPersonaLogin");
        iconoPersonaLogin->setGeometry(QRect(470, 140, 61, 61));
        iconoPersonaLogin->setStyleSheet(QString::fromUtf8("border-image: url(:/images/usuario (4).png);"));
        botonAceptarLogin = new QPushButton(LoginPrincipal);
        botonAceptarLogin->setObjectName("botonAceptarLogin");
        botonAceptarLogin->setGeometry(QRect(440, 340, 111, 31));
        botonAceptarLogin->setMouseTracking(true);
        botonAceptarLogin->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0.0681818 rgba(132, 205, 255, 255), stop:1 rgba(85, 74, 208, 255));\n"
"font: 75 9pt \"Arial\";\n"
"border-radius:25px;\n"
"}\n"
"\n"
"QPushButton:hover{	\n"
"	background-color: qlineargradient(spread:repeat, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(110, 110, 110, 255), stop:1 rgba(255, 255, 255, 255));\n"
"	color: rgb(255, 255, 255);\n"
"    }\n"
"QPushButton:pressed{\n"
"	background-color: rgb(60, 193, 231);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	\n"
"\n"
"\n"
"\n"
"\n"
"\n"
""));
        botonAceptarLogin->setAutoDefault(false);
        esloganLogin = new QLabel(LoginPrincipal);
        esloganLogin->setObjectName("esloganLogin");
        esloganLogin->setGeometry(QRect(80, 350, 311, 16));
        esloganLogin->setStyleSheet(QString::fromUtf8("font: 75 13pt \"Arial\";\n"
"background-color: transparent;\n"
"color: rgb(255, 255, 255);"));
        separadorLogin = new QLabel(LoginPrincipal);
        separadorLogin->setObjectName("separadorLogin");
        separadorLogin->setGeometry(QRect(450, 380, 91, 21));
        separadorLogin->setStyleSheet(QString::fromUtf8("font: 75 10pt \"MS Shell Dlg 2\";\n"
"color: rgb(44, 102, 164);"));
        iconoFBLogin = new QPushButton(LoginPrincipal);
        iconoFBLogin->setObjectName("iconoFBLogin");
        iconoFBLogin->setGeometry(QRect(430, 400, 31, 21));
        iconoFBLogin->setStyleSheet(QString::fromUtf8("border-image: url(:/images/facebook.png);\n"
"background-color: transparent;"));
        iconoGoogleLogin = new QPushButton(LoginPrincipal);
        iconoGoogleLogin->setObjectName("iconoGoogleLogin");
        iconoGoogleLogin->setGeometry(QRect(480, 400, 31, 21));
        iconoGoogleLogin->setStyleSheet(QString::fromUtf8("border-image: url(:/images/google.png);\n"
"background-color: transparent;"));
        iconoTwitterLogin = new QPushButton(LoginPrincipal);
        iconoTwitterLogin->setObjectName("iconoTwitterLogin");
        iconoTwitterLogin->setGeometry(QRect(530, 400, 31, 21));
        iconoTwitterLogin->setStyleSheet(QString::fromUtf8("border-image: url(:/images/twitter.png);\n"
"background-color: transparent;"));
        iconoVolverAtrasLogin = new QPushButton(LoginPrincipal);
        iconoVolverAtrasLogin->setObjectName("iconoVolverAtrasLogin");
        iconoVolverAtrasLogin->setGeometry(QRect(650, 10, 31, 31));
        iconoVolverAtrasLogin->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"border-image: url(:/images/flecha-hacia-atras (1).png);\n"
"background-color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"	background-color: rgb(230, 237, 253);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"	"));
        textoEnlaceRegistro = new QLabel(LoginPrincipal);
        textoEnlaceRegistro->setObjectName("textoEnlaceRegistro");
        textoEnlaceRegistro->setGeometry(QRect(405, 438, 121, 20));
        textoEnlaceRegistro->setStyleSheet(QString::fromUtf8("font: 8pt \"Arial\";\n"
"color: rgb(112, 112, 112);"));
        enlaceRegistrate = new QPushButton(LoginPrincipal);
        enlaceRegistrate->setObjectName("enlaceRegistrate");
        enlaceRegistrate->setGeometry(QRect(525, 438, 61, 20));
        enlaceRegistrate->setStyleSheet(QString::fromUtf8("QPushButton{\n"
"	font: 75 8pt \"Arial\";\n"
"	text-decoration: underline;\n"
"	color: rgb(158, 158, 158);\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"color: rgb(85, 0, 255);\n"
"}"));
        fondoDegradado->raise();
        logoSuperior->raise();
        subContainerLogin->raise();
        cajaUsuarioLogin->raise();
        personasLogin->raise();
        cajaContrasennaLogin->raise();
        textoLogin->raise();
        iconoPersonaLogin->raise();
        botonAceptarLogin->raise();
        esloganLogin->raise();
        separadorLogin->raise();
        iconoFBLogin->raise();
        iconoGoogleLogin->raise();
        iconoTwitterLogin->raise();
        iconoVolverAtrasLogin->raise();
        textoEnlaceRegistro->raise();
        enlaceRegistrate->raise();

        retranslateUi(ContainerLogin);

        botonAceptarLogin->setDefault(false);


        QMetaObject::connectSlotsByName(ContainerLogin);
    } // setupUi

    void retranslateUi(QWidget *ContainerLogin)
    {
        ContainerLogin->setWindowTitle(QCoreApplication::translate("ContainerLogin", "Form", nullptr));
        logoSuperior->setText(QString());
        fondoDegradado->setText(QString());
        subContainerLogin->setText(QString());
        cajaUsuarioLogin->setPlaceholderText(QCoreApplication::translate("ContainerLogin", "Usuario o email", nullptr));
        personasLogin->setText(QString());
        cajaContrasennaLogin->setPlaceholderText(QCoreApplication::translate("ContainerLogin", "Contrase\303\261a", nullptr));
        textoLogin->setText(QCoreApplication::translate("ContainerLogin", "Iniciar sesi\303\263n", nullptr));
        iconoPersonaLogin->setText(QString());
        botonAceptarLogin->setText(QCoreApplication::translate("ContainerLogin", "Aceptar", nullptr));
        esloganLogin->setText(QCoreApplication::translate("ContainerLogin", "\" Ordena tu mundo, desata tu potencial \"", nullptr));
        separadorLogin->setText(QCoreApplication::translate("ContainerLogin", "-------- O -------", nullptr));
        iconoFBLogin->setText(QString());
        iconoGoogleLogin->setText(QString());
        iconoTwitterLogin->setText(QString());
        iconoVolverAtrasLogin->setText(QString());
        textoEnlaceRegistro->setText(QCoreApplication::translate("ContainerLogin", "\302\277No tienes una cuenta?", nullptr));
        enlaceRegistrate->setText(QCoreApplication::translate("ContainerLogin", "Registrate", nullptr));
    } // retranslateUi

};

namespace Ui {
    class ContainerLogin: public Ui_ContainerLogin {};
} // namespace Ui

QT_END_NAMESPACE

#endif // LOGINCZARZK_H
