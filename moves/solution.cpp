#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;
    std::vector<long long> a(n);
    std::vector<long long> b(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> a[i];
    }
    for (int i = 0; i < n; ++i) {
        std::cin >> b[i];
    }

    long long sum_a = 0;
    long long sum_b = 0;
    long long moves = 0;
    for (int i = 0; i < n; ++i) {
        sum_a += a[i];
        sum_b += b[i];
        if (b[i] > a[i]) {
            moves += b[i] - a[i];
        }
    }

    if (sum_a != sum_b) {
        std::cout << -1 << std::endl;
    } else {
        std::cout << moves << std::endl;
    }
    return 0;
}
