function prot(a) {
  this.a = a;
  this.fn1 = function() {
    console.log(this.a);
  }
}

const p = new prot("aasdasd");
p.fn1();