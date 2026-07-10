%global tl_name atendofenv
%global tl_revision 62164

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.2
Release:	%{tl_revision}.1
Summary:	Add a custom symbol at the end of an environment
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/atendofenv
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/atendofenv.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows adding a custom symbol at the end of an environment
(e.g. theorems, definitions, remarks).

