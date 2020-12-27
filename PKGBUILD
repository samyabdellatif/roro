# Maintainer: Samy Abdellatif samiahmed086@gmail.com
pkgname=roro
pkgver=1.0.0
pkgrel=1
pkgdesc="project to learn how to build python distribution packages"
arch=('i686' 'x86_64')
url=""
license=('MIT')
groups=('base-devel')
depends=('')
makedepends=('python-setuptools')
install='roro.install'
source=("local://dist/$pkgname-$pkgver.linux-x86_64.tar.gz")
md5sums=() #autofill using updpkgsums
validpgpkeys=()

build() {
  cd "$pkgname-$pkgver"

  ./configure --prefix=/usr
  make
}
check() {
	cd "$pkgname-$pkgver"
	make -k check
}

package() {
  cd "$pkgname-$pkgver"

  make DESTDIR="$pkgdir/" install
}