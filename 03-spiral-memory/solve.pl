use warnings;
use strict;
use feature qw(say);
use Math::Trig ":pi";

sub get_X_coord {
	my ($n) = @_;
	if ($n == 1) {
		return 0;
	}
	return get_X_coord($n-1) + sin((int(sqrt(4*($n-2)+1)) % 4)*pip2);
};

sub get_Y_coord {
	my ($n) = @_;
	if ($n == 1) {
		return 0;
	}
	return get_Y_coord($n-1) + cos((int(sqrt(4*($n-2)+1)) % 4)*pip2);
};

sub manhattan_distance {
	my ($x, $y) = @_;
	return abs($x) + abs($y);
};

sub print_matrix {
	my ($matrix) = @_;
	foreach my cd $row(@$matrix) {
		say join(" ", @$row);
	}
}

if (@ARGV != 2) {
    exit 1;
}

my $part = $ARGV[0];
my $number = $ARGV[1];

if ($part == 1) {
	my $x = get_X_coord($number);
	my $y = get_Y_coord($number);
	say manhattan_distance($x, $y);
}

if ($part == 2) {
	my @matrix = ([1, 2, 3], [4, 5, 6], [7, 8, 9]);
	print_matrix(\@matrix);
}