$(document).ready(function () {
    var match;
    var chords =
        ['C', 'C#', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B', 'C',
            'Db', 'D', 'D#', 'E', 'F', 'Gb', 'G', 'G#', 'A', 'A#', 'C'];
    var chordRegex = /C#|D#|F#|G#|A#|Db|Eb|Gb|Ab|Bb|C|D|E|F|G|A|B/g;

    var match2;
    var chords2 =
        ['DO', 'DO#', 'RE', 'MIb', 'MI', 'FA', 'FA#', 'SOL', 'LAb', 'LA', 'SIb', 'SI', 'DO',
            'REb', 'RE', 'RE#', 'MI', 'FA', 'SOLb', 'SOL', 'SOL#', 'LA', 'LA#', 'DO'];
    var chordRegex2 = /DO#|RE#|FA#|SOL#|LA#|REb|MIb|SOLb|LAb|SIb|DO|RE|MI|FA|SOL|LA|SI/g;




    $('#transposeUp').click(function () {
        $('.chord0').each(function () {
            var currentChord = $(this).text();
            var output = "";
            var parts = currentChord.split(chordRegex);
            var index = 0;
            while (match = chordRegex.exec(currentChord)) {
                var chordIndex = chords.indexOf(match[0]);
                output += parts[index++] + chords[chordIndex + 1];
            }
            output += parts[index];
            $(this).text(output);

        });


        $('.chord1').each(function () {
            var currentChord2 = $(this).text();
            var output2 = "";
            var parts2 = currentChord2.split(chordRegex2);
            var index2 = 0;
            while (match2 = chordRegex2.exec(currentChord2)) {
                var chordIndex2 = chords2.indexOf(match2[0]);
                output2 += parts2[index2++] + chords2[chordIndex2 + 1];
            }
            output2 += parts2[index2];
            $(this).text(output2);

        });



    });

    $('#transposeDown').click(function () {
        $('.chord0').each(function () {
            var currentChord = $(this).text();
            var output = "";
            var parts = currentChord.split(chordRegex);
            var index = 0;
            while (match = chordRegex.exec(currentChord)) {
                var chordIndex = chords.indexOf(match[0], 1);
                output += parts[index++] + chords[chordIndex - 1];
            }
            output += parts[index];
            $(this).text(output);
        });

        $('.chord1').each(function () {
            var currentChord2 = $(this).text();
            var output2 = "";
            var parts2 = currentChord2.split(chordRegex2);
            var index2 = 0;
            while (match2 = chordRegex2.exec(currentChord2)) {
                var chordIndex2 = chords2.indexOf(match2[0], 1);
                output2 += parts2[index2++] + chords2[chordIndex2 - 1];
            }
            output2 += parts2[index2];
            $(this).text(output2);
        });


    });




});












