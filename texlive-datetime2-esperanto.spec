Name:		texlive-datetime2-esperanto
Version:	47356
Release:	2
Summary:	Esperanto language module for the datetime2 package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/datetime2-esperanto
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-esperanto.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-esperanto.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/datetime2-esperanto.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This module provides the "esperanto" style that can be set
using \DTMsetstyle provided by datetime2.sty. This package is
currently unmaintained. Please see the README for the procedure
to follow if you want to take over the maintenance.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/datetime2-esperanto
%{_texmfdistdir}/tex/latex/datetime2-esperanto
%doc %{_texmfdistdir}/doc/latex/datetime2-esperanto

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
