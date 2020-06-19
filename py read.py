##############################################################################################################################################
print("wich file should be read:")
File = input(str())

a = int(0)
b = int(0)
cc = int(0)
d = int(0)
e = int(0)
f = int(0)
g = int(0)
h = int(0)
i = int(0)
j = int(0)
k = int(0)
l = int(0)
m = int(0)
n = int(0)
oo = int(0)
p = int(0)
q = int(0)
r = int(0)
s = int(0)
t = int(0)
u = int(0)
v = int(0)
w = int(0)
x = int(0)
y = int(0)
z = int(0)
gesamt = int(0)

with open(File) as ff:
  while True:
    c = ff.read(1)
    if c == "a":
        a += 1
        gesamt += 1
    if c == "b":
        b += 1
        gesamt += 1
    if c == "c":
        cc += 1
        gesamt += 1
    if c == "d":
        d += 1
        gesamt += 1
    if c == "e":
        e += 1
        gesamt += 1
    if c == "f":
        f += 1
        gesamt += 1
    if c == "g":
        g += 1
        gesamt += 1
    if c == "h":
        h += 1
        gesamt += 1
    if c == "i":
        i += 1
        gesamt += 1
    if c == "j":
        j += 1
        gesamt += 1
    if c == "k":
        k += 1
        gesamt += 1
    if c == "l":
        l += 1
        gesamt += 1
    if c == "m":
        m += 1
        gesamt += 1
    if c == "n":
        n += 1
        gesamt += 1
    if c == "o":
        oo += 1
        gesamt += 1
    if c == "p":
        p += 1
        gesamt += 1
    if c == "q":
        q += 1
        gesamt += 1
    if c == "r":
        r += 1
        gesamt += 1
    if c == "s":
        s += 1
        gesamt += 1
    if c == "t":
        t += 1
        gesamt += 1
    if c == "u":
        u += 1
        gesamt += 1
    if c == "v":
        v += 1
        gesamt += 1
    if c == "w":
        w += 1
        gesamt += 1
    if c == "x":
        x += 1
        gesamt += 1
    if c == "y":
        y += 1
        gesamt += 1
    if c == "z":
        z += 1
        gesamt += 1
    if not c:
      print ("End of file")
      o = open("Output.txt", "w")
      A = a/gesamt
      A = A * 100
      o.write("A: ")
      o.write('%f' % A)
      o.write("%")
      o.write(" ")
      o.write(str(a))
      o.write(" ")
      B = b/gesamt
      B = B * 100
      o.write("B: ")
      o.write('%f' % B)
      o.write("%")
      o.write(" ")
      o.write(str(b))
      o.write(" ")
      C = cc/gesamt
      C = C * 100
      o.write("C: ")
      o.write('%f' % C)
      o.write("%")
      o.write(" ")
      o.write(str(c))
      o.write(" ")
      D = d/gesamt
      D = D * 100
      o.write("D: ")
      o.write('%f' % D)
      o.write("%")
      o.write(" ")
      o.write(str(d))
      o.write(" ")
      E = e/gesamt
      E = E * 100
      o.write("E: ")
      o.write('%f' % E)
      o.write("%")
      o.write(" ")
      o.write(str(e))
      o.write(" ")
      F = f/gesamt
      F = F * 100
      o.write("F: ")
      o.write('%f' % F)
      o.write("%")
      o.write(" ")
      o.write(str(f))
      o.write(" ")
      G = g/gesamt
      G = G * 100
      o.write("G: ")
      o.write('%f' % G)
      o.write("%")
      o.write(" ")
      o.write(str(g))
      o.write(" ")
      H = h/gesamt
      H = H * 100
      o.write("H: ")
      o.write('%f' % H)
      o.write("%")
      o.write(" ")
      o.write(str(h))
      o.write(" ")
      I = i/gesamt
      I = I * 100
      o.write("I: ")
      o.write('%f' % I)
      o.write("%")
      o.write(" ")
      o.write(str(i))
      o.write(" ")
      J = j/gesamt
      J = J * 100
      o.write("J: ")
      o.write('%f' % J)
      o.write("%")
      o.write(" ")
      o.write(str(j))
      o.write(" ")
      K = k/gesamt
      K = K * 100
      o.write("K: ")
      o.write('%f' % K)
      o.write("%")
      o.write(" ")
      o.write(str(k))
      o.write(" ")
      L = l/gesamt
      L = L * 100
      o.write("L: ")
      o.write('%f' % L)
      o.write("%")
      o.write(" ")
      o.write(str(l))
      o.write(" ")
      M = m/gesamt
      M = M * 100
      o.write("M: ")
      o.write('%f' % M)
      o.write("%")
      o.write(" ")
      o.write(str(m))
      o.write(" ")
      N = n/gesamt
      N = N * 100
      o.write("N: ")
      o.write('%f' % N)
      o.write("%")
      o.write(" ")
      o.write(str(n))
      o.write(" ")
      O = oo/gesamt
      O = O * 100
      o.write("O: ")
      o.write("!")
      o.write('%f' % O)
      o.write("%")
      o.write(" ")
      o.write(str(oo))
      o.write(" ")
      P = p/gesamt
      P = P * 100
      o.write("P: ")
      o.write('%f' % P)
      o.write("%")
      o.write(" ")
      o.write(str(p))
      o.write(" ")
      Q = q/gesamt
      Q = Q * 100
      o.write("Q: ")
      o.write('%f' % Q)
      o.write("%")
      o.write(" ")
      o.write(str(q))
      o.write(" ")
      R = r/gesamt
      R = R * 100
      o.write("R: ")
      o.write('%f' % R)
      o.write("%")
      o.write(" ")
      S = s/gesamt
      S = S * 100
      o.write(str(r))
      o.write(" ")
      o.write("S: ")
      o.write('%f' % S)
      o.write("%")
      o.write(" ")
      T = t/gesamt
      T = T * 100
      o.write(str(s))
      o.write(" ")
      o.write("T: ")
      o.write('%f' % T)
      o.write("%")
      o.write(" ")
      U = u/gesamt
      U = U * 100
      o.write(str(t))
      o.write(" ")
      o.write("U: ")
      o.write('%f' % U)
      o.write("%")
      o.write(" ")
      V = v/gesamt
      V = V * 100
      o.write(str(u))
      o.write(" ")
      o.write("V: ")
      o.write('%f' % V)
      o.write("%")
      o.write(" ")
      W = w/gesamt
      W = W * 100
      o.write(str(v))
      o.write(" ")
      o.write("W: ")
      o.write('%f' % W)
      o.write("%")
      o.write(" ")
      X = x/gesamt
      X = X * 100
      o.write(str(w))
      o.write(" ")
      o.write("X: ")
      o.write('%f' % X)
      o.write("%")
      o.write(" ")
      Y = y/gesamt
      Y = Y * 100
      o.write(str(x))
      o.write("Y: ")
      o.write('%f' % Y)
      o.write("%")
      o.write(" ")
      o.write(str(y))
      o.write(" ")
      Z = z/gesamt
      Z = Z * 100
      o.write("Z: ")
      o.write(str(Z))
      o.write("%")
      o.write(" ")
      o.write('%f' % z)
      o.write(" ")
      o.write(str(gesamt))
      break
