#include <iostream>
#include <fstream>
#include <vector>
#include <string>

void print_matrix(const std::vector<std::vector<char>>& matrix) {
    for (const auto& row : matrix) {
        for (const auto& cell : row) {
            std::cout << cell;
        }
        std::cout << std::endl;
    }
}

bool move_until_obstacle(std::vector<std::vector<char>>& matrix, std::vector<int>& pos, int direction) {
    try {
        if (direction == 0) { // up
            while (matrix.at(pos[0]).at(pos[1]) != '#') {
                matrix.at(pos[0]).at(pos[1]) = 'X';
                pos[0] -= 1;
                // std::cout << "Guard moving up " << pos[0] << ", " << pos[1] << std::endl;
            }
            pos[0] += 1;
        } else if (direction == 1) { // right
            while (matrix.at(pos[0]).at(pos[1]) != '#') {
                matrix.at(pos[0]).at(pos[1]) = 'X';
                pos[1] += 1;
                // std::cout << "Guard moving right " << pos[0] << ", " << pos[1] << std::endl;
            }
            pos[1] -= 1;
        } else if (direction == 2) { // down
            while (matrix.at(pos[0]).at(pos[1]) != '#') {
                matrix.at(pos[0]).at(pos[1]) = 'X';
                pos[0] += 1;
                // std::cout << "Guard moving down " << pos[0] << ", " << pos[1] << std::endl;
            }
            pos[0] -= 1;
        } else if (direction == 3) { // left
            while (matrix.at(pos[0]).at(pos[1]) != '#') {
                matrix.at(pos[0]).at(pos[1]) = 'X';
                pos[1] -= 1;
                // std::cout << "Guard moving left " << pos[0] << ", " << pos[1] << std::endl;
            }
            pos[1] += 1;
        }
    } catch (const std::out_of_range&) {
        std::cout << "Guard exited the matrix" << std::endl;
        return true;
    }

    // std::cout << "Guard hit an obstacle" << std::endl;
    return false;
}

void func() {
    std::vector<std::vector<char>> matrix;
    std::vector<int> init_pos;
    std::ifstream infile("input.txt");
    std::string line;

    while (std::getline(infile, line)) {
        matrix.push_back(std::vector<char>(line.begin(), line.end()));
        if (init_pos.empty()) {
            for (size_t i = 0; i < line.size(); ++i) {
                if (line[i] == '^') {
                    init_pos = {static_cast<int>(matrix.size()) - 1, static_cast<int>(i)};
                }
            }
        }
    }

    print_matrix(matrix);
    std::cout << "Initial position: " << init_pos[0] << ", " << init_pos[1] << std::endl;

    bool exited = false;
    int direction = 0;

    int counter = 0;
    while (!exited) {
        exited = move_until_obstacle(matrix, init_pos, direction);
        direction = (direction + 1) % 4;
        std::cout << "Guard moved to [" << init_pos[0] << ", " << init_pos[1] << "]" << std::endl;
    }

    // int counter = 0;
    for (const auto& row : matrix) {
        for (const auto& cell : row) {
            if (cell == 'X') {
                counter += 1;
            }
        }
    }

    std::cout << "Guard moved " << counter << " steps" << std::endl;
}

int main() {
    func();
    return 0;
}