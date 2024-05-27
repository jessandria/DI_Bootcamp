let pattern = '';
for (let i = 1; i <= 6; i++) {
    for (let j = 1; j <= i; j++) {
        pattern += '* ';
    }
    pattern = pattern.trim() + '\n';
}
console.log(pattern);
