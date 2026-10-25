
x = list(map(float, input("Enter X values separated by spaces: ").split()))
y = list(map(float, input("Enter Y values separated by spaces: ").split()))

if len(x) != len(y) or len(x) < 2:
    print("Enter equal numbers of X and Y values, at least two.")
    raise SystemExit

n = len(x)
mx = sum(x) / n
my = sum(y) / n

den = sum((a - mx) ** 2 for a in x)

if den == 0:
    print("X values must not all be equal.")
    raise SystemExit

m = sum((x[i] - mx) * (y[i] - my)
        for i in range(n)) / den
c = my - m * mx

pred = [m * a + c for a in x]
mse = sum((y[i] - pred[i]) ** 2 for i in range(n)) / n
mae = sum(abs(y[i] - pred[i]) for i in range(n)) / n

total = sum((a - my) ** 2 for a in y)
r2 = 1 - sum((y[i] - pred[i]) ** 2
             for i in range(n)) / total if total else 1

print("\nLinear Regression")
print("Slope:", round(m, 2))
print("Intercept:", round(c, 2))
print("Predictions:", pred)
print("MSE:", round(mse, 2))
print("MAE:", round(mae, 2))
print("R2 Score:", round(r2, 2))

new_x = float(input("Enter X for prediction: "))
print("Predicted Y:", round(m * new_x + c, 2))

print("\nPolynomial features (X, X squared):")
for a in x:
    print(a, a ** 2)
