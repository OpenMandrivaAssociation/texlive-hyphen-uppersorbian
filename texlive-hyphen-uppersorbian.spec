%global tl_name hyphen-uppersorbian
%global tl_revision 78069

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Upper Sorbian hyphenation patterns.
Group:		Publishing
URL:		https://www.ctan.org/pkg/hyphen-uppersorbian
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/hyphen-uppersorbian.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(hyph-utf8)
Requires:	texlive(hyphen-base)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Hyphenation patterns for Upper Sorbian in T1/EC and UTF-8 encodings.

