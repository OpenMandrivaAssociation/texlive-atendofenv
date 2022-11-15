Name:		texlive-atendofenv
Version:	62164
Release:	1
Summary:	Add a custom symbol at the end of an environment
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/atendofenv
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package allows adding a custom symbol at the end of an
environment (e.g. theorems, definitions, remarks).

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/atendofenv
%{_texmfdistdir}/tex/latex/atendofenv
%doc %{_texmfdistdir}/doc/latex/atendofenv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
