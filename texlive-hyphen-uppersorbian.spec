# revision 23085
# category TLCore
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-hyphen-uppersorbian
Version:	20111103
Release:	1
Summary:	Upper Sorbian hyphenation patterns
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-uppersorbian.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-hyphen-base
Requires:	texlive-hyph-utf8

%description
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8
encodings.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%_texmf_language_dat_d/hyphen-uppersorbian
%_texmf_language_def_d/hyphen-uppersorbian
%_texmf_language_lua_d/hyphen-uppersorbian

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmf_language_dat_d}
cat > %{buildroot}%{_texmf_language_dat_d}/hyphen-uppersorbian <<EOF
\%\% from hyphen-uppersorbian:
uppersorbian loadhyph-hsb.tex
EOF
mkdir -p %{buildroot}%{_texmf_language_def_d}
cat > %{buildroot}%{_texmf_language_def_d}/hyphen-uppersorbian <<EOF
\%\% from hyphen-uppersorbian:
\addlanguage{uppersorbian}{loadhyph-hsb.tex}{}{2}{2}
EOF
mkdir -p %{buildroot}%{_texmf_language_lua_d}
cat > %{buildroot}%{_texmf_language_lua_d}/hyphen-uppersorbian <<EOF
-- from hyphen-uppersorbian:
	['uppersorbian'] = {
		loader = 'loadhyph-hsb.tex',
		lefthyphenmin = 2,
		righthyphenmin = 2,
		synonyms = {  },
		patterns = 'hyph-hsb.pat.txt',
		hyphenation = 'hyph-hsb.hyp.txt',
	},
EOF
