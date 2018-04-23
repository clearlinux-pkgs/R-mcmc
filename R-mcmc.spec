#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mcmc
Version  : 0.9.5
Release  : 3
URL      : https://cran.r-project.org/src/contrib/mcmc_0.9-5.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mcmc_0.9-5.tar.gz
Summary  : Markov Chain Monte Carlo
Group    : Development/Tools
License  : MIT
Requires: R-mcmc-lib
Requires: R-Iso
Requires: R-xtable
BuildRequires : R-Iso
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
Markov chain Monte Carlo (MCMC).  Users specify the distribution by an
    R function that evaluates the log unnormalized density.  Algorithms
    are random walk Metropolis algorithm (function metrop), simulated
    tempering (function temper), and morphometric random walk Metropolis

%package lib
Summary: lib components for the R-mcmc package.
Group: Libraries

%description lib
lib components for the R-mcmc package.


%prep
%setup -q -c -n mcmc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523744397

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1523744397
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library mcmc|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/mcmc/DESCRIPTION
/usr/lib64/R/library/mcmc/INDEX
/usr/lib64/R/library/mcmc/LICENSE
/usr/lib64/R/library/mcmc/Meta/Rd.rds
/usr/lib64/R/library/mcmc/Meta/data.rds
/usr/lib64/R/library/mcmc/Meta/features.rds
/usr/lib64/R/library/mcmc/Meta/hsearch.rds
/usr/lib64/R/library/mcmc/Meta/links.rds
/usr/lib64/R/library/mcmc/Meta/nsInfo.rds
/usr/lib64/R/library/mcmc/Meta/package.rds
/usr/lib64/R/library/mcmc/Meta/vignette.rds
/usr/lib64/R/library/mcmc/NAMESPACE
/usr/lib64/R/library/mcmc/R/mcmc
/usr/lib64/R/library/mcmc/R/mcmc.rdb
/usr/lib64/R/library/mcmc/R/mcmc.rdx
/usr/lib64/R/library/mcmc/data/foo.txt.gz
/usr/lib64/R/library/mcmc/data/logit.txt.gz
/usr/lib64/R/library/mcmc/designDoc/metrop.tex
/usr/lib64/R/library/mcmc/designDoc/temper.tex
/usr/lib64/R/library/mcmc/doc/bfst.R
/usr/lib64/R/library/mcmc/doc/bfst.Rnw
/usr/lib64/R/library/mcmc/doc/bfst.pdf
/usr/lib64/R/library/mcmc/doc/debug.R
/usr/lib64/R/library/mcmc/doc/debug.Rnw
/usr/lib64/R/library/mcmc/doc/debug.pdf
/usr/lib64/R/library/mcmc/doc/demo.R
/usr/lib64/R/library/mcmc/doc/demo.Rnw
/usr/lib64/R/library/mcmc/doc/demo.pdf
/usr/lib64/R/library/mcmc/doc/index.html
/usr/lib64/R/library/mcmc/doc/metrop.pdf
/usr/lib64/R/library/mcmc/doc/morph.R
/usr/lib64/R/library/mcmc/doc/morph.Rnw
/usr/lib64/R/library/mcmc/doc/morph.pdf
/usr/lib64/R/library/mcmc/doc/temper.pdf
/usr/lib64/R/library/mcmc/help/AnIndex
/usr/lib64/R/library/mcmc/help/aliases.rds
/usr/lib64/R/library/mcmc/help/mcmc.rdb
/usr/lib64/R/library/mcmc/help/mcmc.rdx
/usr/lib64/R/library/mcmc/help/paths.rds
/usr/lib64/R/library/mcmc/html/00Index.html
/usr/lib64/R/library/mcmc/html/R.css
/usr/lib64/R/library/mcmc/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mcmc/libs/mcmc.so
/usr/lib64/R/library/mcmc/libs/mcmc.so.avx2
/usr/lib64/R/library/mcmc/libs/mcmc.so.avx512
