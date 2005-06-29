%define		_arch	i386
%define		_pver	4.1

Summary:	Linux Terminal Server Project - Core system for terminals
Summary(pl):	Podstawowy system dla terminali z Linux Terminal Server Project
Name:		ltsp_x336
Version:	4.0.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	http://www.ltsp.org/ltsp-utils-0.11.tgz
# Source0-md5:	b17b350b18b04d769fcadcd12885a573
Source1:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_S3_S3V-1.1-0-%{_arch}.tgz
# Source1-md5:	22d4621368208c11e1fdd9c484cf43c8
Source2:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_3DLabs-1.1-0-%{_arch}.tgz
# Source2-md5:	804e7ccb0147c9c764a71ca1a92f2f7d
Source3:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_Mach8-1.1-0-%{_arch}.tgz
# Source3-md5:	3135708ea8a2c88af9d0da487d95ca3a
Source4:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_Mono-1.1-0-%{_arch}.tgz
# Source4-md5:	6dc5c7997d6f5e023e3089483e161267
Source5:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_AGX-1.1-0-%{_arch}.tgz
# Source5-md5:	b97b75836f18052666daf7e0a6fbf1ae
Source6:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_W32-1.1-0-%{_arch}.tgz
# Source6-md5:	3c702fa02140f45c0a076ba8da6afa78
Source7:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_Mach32-1.1-0-%{_arch}.tgz
# Source7-md5:	c86a3aa4475dd72166676ab2663ea4ae
Source8:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_VGA16-1.1-0-%{_arch}.tgz
# Source8-md5:	a746dd6c7b1b025f8ce328f6a4f4885d
Source9:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_P9000-1.1-0-%{_arch}.tgz
# Source9-md5:	16c7a31cacbdf16bbffd23d143c8b195
Source10:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_Mach64-1.1-0-%{_arch}.tgz
# Source10-md5:	768afad166b59aa5cf636dddce43ed3e
Source11:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_8514-1.1-0-%{_arch}.tgz
# Source11-md5:	30ee951ff0b1c495ceda5beec71273a7
Source12:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_I128-1.1-0-%{_arch}.tgz
# Source12-md5	c61062f9900037068388a98267f9cc0c
Source13:	http://ltsp.mirrors.tds.net/pub/ltsp/ltsp-%{_pver}/ltsp-x336_SVGA-1.1-0-%{_arch}.tgz
# Source13-md5:	7ba7ad7f7c652cde4bf19d1a5e9be5bf
URL:		http://www.ltsp.org/
Requires:	ltsp_core
AutoProv:	0
AutoReq:	0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_ltspdir	/home/services/ltsp

%description
LTSP is an add-on package for Linux that allows you to connect lots of
low-powered thin client terminals to a Linux server. Applications
typically run on the server and accept input and display their output
on the thin client display. LTSP is available as a set of packages that
can be installed on any Linux system.

This package contains x366 for LTSP terminals.

%description -l pl
- Jak obni¿yæ koszty I ocaliæ planetê?
- Przekszta³ciæ te stare pecety na X-terminale z u¿yciem LTSP.

Ten pakiet zawiera x366 dla terminali LTSP.

%prep
%setup -q -n ltsp-utils

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_ltspdir}
tar zxf %{SOURCE1}
tar zxf %{SOURCE2}
tar zxf %{SOURCE3}
tar zxf %{SOURCE4}
tar zxf %{SOURCE5}
tar zxf %{SOURCE6}
tar zxf %{SOURCE7}
tar zxf %{SOURCE8}
tar zxf %{SOURCE9}
tar zxf %{SOURCE10}
tar zxf %{SOURCE11}
tar zxf %{SOURCE12}
tar zxf %{SOURCE13}
cd i386
cp -r usr $RPM_BUILD_ROOT%{_ltspdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc README
%dir %{_ltspdir}
%attr(755,root,root) %{_ltspdir}/usr/X11R6
