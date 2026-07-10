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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package allows adding a custom symbol at the end of an environment
(e.g. theorems, definitions, remarks).

%prep
%setup -q -c -a1 -a2
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/source
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/source/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/atendofenv
%dir %{_datadir}/texmf-dist/source/latex/atendofenv
%dir %{_datadir}/texmf-dist/tex/latex/atendofenv
%doc %{_datadir}/texmf-dist/doc/latex/atendofenv/LICENSE
%doc %{_datadir}/texmf-dist/doc/latex/atendofenv/README.md
%doc %{_datadir}/texmf-dist/doc/latex/atendofenv/atendofenv.pdf
%doc %{_datadir}/texmf-dist/source/latex/atendofenv/atendofenv.dtx
%doc %{_datadir}/texmf-dist/source/latex/atendofenv/atendofenv.ins
%{_datadir}/texmf-dist/tex/latex/atendofenv/atendofenv.sty
