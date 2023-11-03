#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-mcmc
Version  : 0.9.7
Release  : 49
URL      : https://cran.r-project.org/src/contrib/mcmc_0.9-7.tar.gz
Source0  : https://cran.r-project.org/src/contrib/mcmc_0.9-7.tar.gz
Summary  : Markov Chain Monte Carlo
Group    : Development/Tools
License  : MIT
Requires: R-mcmc-lib = %{version}-%{release}
BuildRequires : R-Iso
BuildRequires : R-xtable
BuildRequires : buildreq-R

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
cd %{_builddir}/mcmc

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641055841

%install
export SOURCE_DATE_EPOCH=1641055841
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -ftree-vectorize -mno-vzeroupper  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library mcmc
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc mcmc || :


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
/usr/lib64/R/library/mcmc/tests/accept-batch.R
/usr/lib64/R/library/mcmc/tests/accept-batch.Rout.save
/usr/lib64/R/library/mcmc/tests/circle.R
/usr/lib64/R/library/mcmc/tests/circle.Rout.save
/usr/lib64/R/library/mcmc/tests/initseq.R
/usr/lib64/R/library/mcmc/tests/initseq.Rout.save
/usr/lib64/R/library/mcmc/tests/isotropic.R
/usr/lib64/R/library/mcmc/tests/isotropic.Rout.save
/usr/lib64/R/library/mcmc/tests/logit.R
/usr/lib64/R/library/mcmc/tests/logit.Rout.save
/usr/lib64/R/library/mcmc/tests/logitbat.R
/usr/lib64/R/library/mcmc/tests/logitbat.Rout.save
/usr/lib64/R/library/mcmc/tests/logitfun.R
/usr/lib64/R/library/mcmc/tests/logitfun.Rout.save
/usr/lib64/R/library/mcmc/tests/logitfunarg.R
/usr/lib64/R/library/mcmc/tests/logitfunarg.Rout.save
/usr/lib64/R/library/mcmc/tests/logitidx.R
/usr/lib64/R/library/mcmc/tests/logitidx.Rout.save
/usr/lib64/R/library/mcmc/tests/logitlogidx.R
/usr/lib64/R/library/mcmc/tests/logitlogidx.Rout.save
/usr/lib64/R/library/mcmc/tests/logitmat.R
/usr/lib64/R/library/mcmc/tests/logitmat.Rout.save
/usr/lib64/R/library/mcmc/tests/logitnegidx.R
/usr/lib64/R/library/mcmc/tests/logitnegidx.Rout.save
/usr/lib64/R/library/mcmc/tests/logitsub.R
/usr/lib64/R/library/mcmc/tests/logitsub.Rout.save
/usr/lib64/R/library/mcmc/tests/logitsubbat.R
/usr/lib64/R/library/mcmc/tests/logitsubbat.Rout.save
/usr/lib64/R/library/mcmc/tests/logitvec.R
/usr/lib64/R/library/mcmc/tests/logitvec.Rout.save
/usr/lib64/R/library/mcmc/tests/morph.R
/usr/lib64/R/library/mcmc/tests/morph.Rout.save
/usr/lib64/R/library/mcmc/tests/morph.metrop.R
/usr/lib64/R/library/mcmc/tests/morph.metrop.Rout.save
/usr/lib64/R/library/mcmc/tests/morphtoo.R
/usr/lib64/R/library/mcmc/tests/morphtoo.Rout.save
/usr/lib64/R/library/mcmc/tests/saveseed.R
/usr/lib64/R/library/mcmc/tests/saveseed.Rout.save
/usr/lib64/R/library/mcmc/tests/saveseedmorph.R
/usr/lib64/R/library/mcmc/tests/saveseedmorph.Rout.save
/usr/lib64/R/library/mcmc/tests/temp-par-witch.R
/usr/lib64/R/library/mcmc/tests/temp-par.R
/usr/lib64/R/library/mcmc/tests/temp-par.Rout.save
/usr/lib64/R/library/mcmc/tests/temp-ser-witch.R
/usr/lib64/R/library/mcmc/tests/temp-ser-witch.Rout.save
/usr/lib64/R/library/mcmc/tests/temp-ser.R
/usr/lib64/R/library/mcmc/tests/temp-ser.Rout.save

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/mcmc/libs/mcmc.so
/usr/lib64/R/library/mcmc/libs/mcmc.so.avx2
/usr/lib64/R/library/mcmc/libs/mcmc.so.avx512
